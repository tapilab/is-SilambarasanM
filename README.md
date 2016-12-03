## Problem

Link Prediction based on Brand Perception. Build a recommendation system to predict a brand of attribute (like eco-friendliness, nutritious or luxury) similar to the brands being followed by a user on Twitter.

![Image](/src/figures/logos.png)

## Research questions


1. What is the perceived attribute value for a brand? How to measure it using Social Media Network?
2. How to measure the similarity of two brands with respect to an 'attribute'?
3. How does a marketing decision made by a brand impacts its perceived attribute rating?

## Related work

1. [Mining Brand Perceptions from Twitter Social Networks](http://pubsonline.informs.org/doi/10.1287/mksc.2015.0968)
2. [The Link Prediction Problem for Social Networks](https://www.cs.cornell.edu/home/kleinber/link-pred.pdf)

## Data

A list of Twitter handles of popular brands in United States were chosen from different sectors like Personal Care, Food, Household Chemicals, Electronic Appliance, Apparel and Car. There were 1404 brands collected for this work. For each Twitter account, the list of Follower IDs were collected using Twitter API and stored in a tab separated format. Each row represents an adjacency list form of followers list for a brand. First column is the Twitter handle of the brand and rest of the row is the list of follower ids with a maximum limit of 500000 followers.

*Sample Record:*

`conair_hair 2461773146  125072777 743873850 2163652136`

`conair_hair` is the Twitter handle and `2461773146`, `125072777`, `743873850`, `2163652136` are ids of followers who follow *Conair* brand on Twitter.
## Methods

1. Collected the follower ids for the chosen brands Twitter accounts using Twitter API and stored in a text file.
2. Calculated the Jaccard similarity based on the list of followers collected for each brand-brand pair.
3. Training data was obtained with samples for positive and negative labels. An actual brand-follower link observed in the data was removed and used as a positive sample. A brand not followed by a follower was added as a negative sample.
4. A baseline Logistic Regression Classifier was built using training data with positive and negative labels and the performance was evaluated.

## Results

**Ranking based on Jaccard Scores**

* Average Rank of positive samples: 10.7

![Image](/src/figures/jsrp.png)

* Average rank of negative samples: 97.7

![Image](/src/figures/jsrn.png)

**Baseline Classifier**

* Logistic Regression using SGDClassifier

* Training Samples: 4868 (positive samples-2434, negavtive-2434)

* Training Accuracy: 86.1%

**Evaluation**

* Test Samples: 812 (with k = 25, #samples = 812 x 25)

* Test Accuracy:
  * 49.02% (Classifier Accuracy)
  * 40.39% (Overall System Accuracy)


## Conclusions / Future Work

Here's the main conclusions and a list of directions for improvement.

* Consider additional attributes for scoring to choose the candidates. For eg. purchasing behavior of consumers.
* More research on the finding features for the classifier, consider adding sector specific attributes to improve the performance.
* Analyze user tweets to consider users’ perception for predicting the brand.
More research on the parameters for the classifier.
* Remove bots from the followers list to minimize the noise.
