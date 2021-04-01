!pip install tweepy
import tweepy as tw

!pip install ConfigParser
import configparser

import os
import time
import json
import pandas as pd

#reads keys and tokens for Twitter API

from google.colab import drive
drive.mount('/content/gdrive')

!ls "/content/gdrive/MyDrive/Colab Notebooks/twitterapp-ozgem.txt"  #reads the text file from Drive OR add your own directory. 

config=configparser.RawConfigParser()
config.read(filenames= r'/content/gdrive/MyDrive/Colab Notebooks/twitterapp-ozgem.txt')
print(config.sections())

access_token=config.get("twitterapp_ozgem", "access_token")
access_token_secret=config.get('twitterapp_ozgem', "access_token_secret")
consumer_key=config.get('twitterapp_ozgem', "consumer_key")
consumer_secret=config.get('twitterapp_ozgem',"consumer_secret")

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret) 
api = tw.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#the following code obtains follower's user objects and save as a json file.

screen_name ="SCREEN_NAME" #Insert the screen name that you want to get followers from.

json_file = open("DATE-SCREEN_NAME-ozgem.json", "a")
for follower in tw.Cursor(api.followers, screen_name).items():
  json_str = json.dumps(follower._json)
  json_file.write(json_str + "\n")
