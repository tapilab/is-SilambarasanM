
# coding: utf-8

# In[1]:

import ConfigParser
import sys
import time
from TwitterAPI import TwitterAPI


# In[2]:

def get_twitter(config_file):
    config = ConfigParser.ConfigParser()
    config.read(config_file)
    twitter = TwitterAPI(
                   config.get('twitter', 'consumer_key'),
                   config.get('twitter', 'consumer_secret'),
                   config.get('twitter', 'access_token'),
                   config.get('twitter', 'access_token_secret'))
    return twitter

twitter = get_twitter('twitter.cfg')
print('Established Twitter connection.')


# In[3]:

def read_brands(filename):
    brands = []
    with open(filename) as data_file:
        for row in data_file:
            brands.append(row.strip())
    return brands
    
brands = read_brands('correct_brand_names.txt')
print('Read %d brands' % len(brands))


# In[4]:

def robust_request(twitter, resource, params, max_tries=5):
    for i in range(max_tries):
        request = twitter.request(resource, params)
        if request.status_code == 200:
            return request
        elif request.status_code == 34:
            print("Account",params['screen_name'],"doesn't exist.")
            return None
        else:
            print ('Got error:', request.text, '\nsleeping for 15 minutes.')
            sys.stderr.flush()
            time.sleep(61 * 15)


# In[5]:

def get_followers(screen_name):
    #See https://dev.twitter.com/rest/reference/get/followers/ids
    next_cursor = -1
    followers = set()
	
    while next_cursor != 0 and len(followers) < 500000:
        request = robust_request(twitter,"followers/ids", {'screen_name':screen_name,'cursor':next_cursor,'count':5000})
        if request is None:
            return []
        response = eval(str(request.json()))
        followers = followers | set(response['ids'])
        next_cursor = response['next_cursor']
        print ('Retrieved %d followers so far...'%len(followers))
    return followers


# In[ ]:
import os
out_file = open("brand_followers_corrected.tsv","w")
for b in brands:
    followers = get_followers(b)
    data = b + '\t'+ '\t'.join([str(f) for f in followers]) + '\n'
    out_file.write(data)
    print('Written',b)
    out_file.flush()
    os.fsync(out_file.fileno())
    sys.stdout.flush()
out_file.close()


# In[ ]:



