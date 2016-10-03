import numpy as np
from sklearn.cluster.k_means_ import k_means
from sklearn.preprocessing import scale
from sklearn.utils import graph as graphutil
from sklearn.utils.arpack import eigsh
from sklearn.utils import check_random_state

class MySpectralClustering:
    """
    Cluster 100 nodes into 2 clusters. We set the affinities so that the first
    50 nodes have similarity .99, as do the second 50.

    >>> from scipy.sparse import csr_matrix
    >>> from itertools import combinations
    >>> affinities = csr_matrix(np.ones(10000).reshape(100, 100) * .001)
    >>> c1 = range(50)
    >>> c2 = range(50,100)
    >>> for i, j in combinations(c1, 2):
    ...   affinities[i, j] = affinities[j, i] = .99
    >>> for i, j in combinations(c2, 2):
    ...   affinities[i, j] = affinities[j, i] = .99
    >>> cl = MySpectralClustering(k=2, n_components=10)
    >>> clusters = cl.cluster(affinities)
    >>> set(clusters[:50])
    {1}
    >>> set(clusters[50:])
    {0}
    """
    def __init__(self,
                 k,
                 n_components=None,
                 rand=check_random_state(123456),
                 tol=0,
                 init_centroids='k-means++',
                 n_init=10,
                 do_scale=False):

        self.k = k
        self.n_components = n_components if n_components else k
        self.rand = rand
        self.tol = tol
        self.init_centroids = init_centroids
        self.do_scale = do_scale
        self.n_init = n_init

    def embed(self, laplacian, diagonal, k, tol=0):
        k = k + 1
        lambdas, diffusion_map = eigsh(-laplacian, k=k,
                                       which='SM',
                                       tol=tol)
        embedding = diffusion_map.T[k::-1] * diagonal
        if self.do_scale:
            return scale(embedding[1:k].T, axis=1)
        else:
            return embedding[1:k].T

    def cluster(self, affinities):
        laplacian, diagonal = graphutil.graph_laplacian(affinities,
                                                        normed=True,
                                                        return_diag=True)

        self.embedding = self.embed(laplacian,
                                    diagonal,
                                    self.k,
                                    self.tol)

        centroid_vals, self.labels, _ = k_means(self.embedding,
                                                self.k,
                                                random_state=self.rand,
                                                n_init=self.n_init,
                                                init=self.init_centroids)

        self.centroids = []
        for c in centroid_vals:
            self.centroids.append(np.argmin([np.sum((c - e) ** 2) for e in self.embedding]))

        return self.labels

