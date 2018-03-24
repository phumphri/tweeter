# Set dependancies
import tweepy
import json
import os

# Set Twitter credentials.

consumer_key = os.environ['consumer_key']
consumer_secret = os.environ['consumer_secret']
access_token = os.environ['access_token']
access_token_secret = os.environ['access_token_secret']

# Set Authentication Handler
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.access_token_secret(access_token, access_token_secret)

# The original version from YouTube.
# Returned is an object with methods.
# api = tweepy.API(auth) # My original version.
# user_object api.me()
# print(user_object.name)

# auth_handler – authentication handler to be used.
# parser – The object to use for parsing the response from Twitter.
# With this version, tweepy returns everything as type dict.
api = tweepy.API(auth_handler=auth, parser=tweepy.parsers.JSONParser())

# Verify that twitter context has been set.
# In this version, everything returned is type dict.
user_object = api.me()
# print(json.dumps(user_object, indent=4, sort_keys=True))
print(user_object.get('name'))
