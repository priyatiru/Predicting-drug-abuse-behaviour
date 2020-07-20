# Predicting-drug-abuse-behaviour
This repository contains all the code files and output of the project carried out on the topic- Predicting Drug Abuse Behavior using Deep Learning technologies. The keywords used in the project are -  drugs, BERT, Tweepy, Twitter, timeline, students, depression, bag of words, drug abuse behavior, hash, cosine  similarities, LDA, multinomial naive bayes, linear support vector machine, random forest classifier, NLP, deep learning.

# Following are the descriptions of the codes contained in the repository :
1. #getTweets - 
Looks for timelines and fetches the tweet texts
For the authentication of the Tweepy API required
consumer and access keys and tokens should be
obtained from an active Twitter's Developer account. (Environment- Jupyter notebook, Libraries imported were tweepy, pandas,
os, json)

2. #cleaning -
Preprocessing the user timeline tweets. (Environment- Jupyter notebook, Libraries imported were nltk.stem,
nltk.tokenize)

3. #LDA -
Fetching 10 clouds of 15 words from the clean timeline
data. (Environment- IDLE (Python
3.7), Library imported was gensim )

4. #clearlda-
Removing extras from lda output. (Environment- Jupyter notebook, Library imported was pandas)

5. #randomDivisionOfBow -
Randomly dividing 120 words of BoW into 8 lines of 15 words each. (Environment- Jupyter notebook, Libraries imported were pandas,random)

6. #ComputingSimilarities-
Extracting the sentence embeddings of both the 10 clouds of 15 words and the BoW. Computing the cosine similarities of the pair of sentence embeddings. 8 values similarity indices will be there for each cloud of 15 words,averaging it to a single similarity index. (Environment- Google colab, Libraries imported were torch,pytorch_pretrained_bert,sklearn)

7. #targetTweets-
Comparing similarity indices of clouds of words. Fetching target tweets and saving in a CSV file. (Environment- Jupyter Notebook, Libraries imported were pandas , json)

8. #BoW -
Creating a bag of words using drugMen.csv and ddd.txt files which containing paragraphs of some articles and clean tweets related to drugs.






