# Let's first import all the libraries used in this project.
# textblob - is an NLP library that can extract patterns in text and classify them. It can classify text in a range
# from [-1,1]. -1 for negative emotions and +1 for positive emotions. It can identify the polarity and subjectivity of
# words from a text. For example - exclaimation marks, emojis often are given from [0,1] as it presumably denotes
# positive emotions.
import pandas as pd
import numpy as np
import tweepy # Twitter library
import wordcloud
import textblob
import regex as re
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

path = "C:/Users/theme/Desktop/NLP projects/env.CSV" # Where the API keys are stored. Directly declaring the keys in the
# code is a big no no. Hence, we store it in a .csv file so that only local host can access it.
log = pd.read_csv(path) # Pandas library is used to read csv file formats
# Let's read the keys and store it in their respective variables.
consumer_key = log['key'][0]
secret_consumer_key = log['key'][1]
access_token = log['key'][2]
secret_access_token = log['key'][3]

authenticate = tweepy.OAuthHandler(consumer_key, secret_consumer_key) # Authenticate object takes in consumer keys.
authenticate.set_access_token(access_token, secret_access_token)
api = tweepy.API(authenticate, wait_on_rate_limit= True) # API is set from the keys stored in authenticate object.
# Next, we need to create our database to analyze from. In this case, let's say we'll take a 100 tweets from a public
# twitter handle. Bill Gates, for example, and analyze a 100 of his tweets.
posts = api.user_timeline(screen_name = 'BillGates', count = 100, lang = 'en', tweet_mode = 'extended')
# Screen name is the unique ID ("@user_id") also known as a Twitter handle and not the public name which is not unique
# to a user. The user_timeline attribute gives access to a specific user's timeline.
print("Showing 5 most recent tweets by Bill Gates")
i = 1 # putting it outside the loop, as if I declare "i" inside, on a second iteration of the loop, i becomes 1 again
# and we don't want that.

for tweet in posts[0:5]:
    print(str(i) + ")" + tweet.full_text + '\n')
    i = i+1
