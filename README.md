## Problem

Build a Recommendation System to predict a brand of attribute (like eco-friendliness, nutritious or luxury) similar to the brands being followed by a user on Twitter.

## Research questions


1. What is the perceived attribute value for a brand? How to measure it using Social Media Network?
2. How similar are two brands with respect to an attribute?
3. How does a marketing decision made by a brand impacts its perceived attribute rating?

## Related work


1. [Mining Brand Perceptions from Twitter Social Networks](http://pubsonline.informs.org/doi/10.1287/mksc.2015.0968)
2. [The Link Prediction Problem for Social Networks](https://www.cs.cornell.edu/home/kleinber/link-pred.pdf)

## Data

A list of Twitter handles of popular brands in United States were chosen from different sectors like Personal Care, Food, Household Chemicals, Electronic Appliance, Apparel and Car. There were 1440 brands collected for this work. For each Twitter account, the list of Follower IDs were collected using Twitter API and stored in a tab separated format. Each row represents an adjacency list form of followers list for a brand. First column is the Twitter handle of the brand and rest of the row is the list of follower ids with a maximum limit of 500000 followers.

*Sample Record:*

`conair_hair 2461773146  125072777 743873850 2163652136`

`conair_hair` is the Twitter handle and `2461773146`, `125072777`, `743873850`, `2163652136` are ids of followers who follow *Conair* brand on Twitter.
## Methods

1. Collected the follower ids for the chosen brands Twitter accounts using Twitter API and stored in a text file.
2. Calculated the Jaccard similarity based on the list of followers collected for each brand-brand pair.
3. Training data was obtained with samples for positive and negative labels. An actual brand-follower link observed in the data was removed and used as a positive sample. A brand not followed by a follower was added as a negative sample.
4. A baseline Logistic Regression Classifier was built using training data with positive and negative labels and the performance was evaluated.

## Results

Here is a summary of the main results.

You can include an image like this:

![Image](/blob/master/src/figures/iit.png?raw=true)

## Conclusions / Future Work

Here's the main conclusions and a list of directions for improvement.
