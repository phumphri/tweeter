# Set dependancies
import tweepy
from tweepy.auth import OAuthHandler
import json
import os

# Set Twitter credentials.

consumer_key = os.environ.get('consumer_key')
consumer_secret = os.environ.get('consumer_secret')
access_token = os.environ.get('access_token')
access_token_secret = os.environ.get('access_token_secret')

# Set Authentication Handler
try:
    auth = OAuthHandler(consumer_key, consumer_secret)
    
except Exception as e:
    print("OAuthHandler threw an Exception:")
    for arg in e.args:
        print(arg)
    pass

try:
    auth.set_access_token(access_token, access_token_secret)
    
except Exception as e:
    print("auth.set_access_token threw an Exception:")
    for arg in e.args:
        print(arg)
    pass

# auth_handler – authentication handler to be used.
# parser – The object to use for parsing the response from Twitter.
# With this version, tweepy returns everything as type dict.
try:
    api = tweepy.API(auth_handler=auth, parser=tweepy.parsers.JSONParser())

except Exception as e:
    print("tweepy.API threw an Exception:")
    for arg in e.args:
        print(arg)
    pass


# Verify that twitter context has been set.
# In this version, everything returned is type dict.
try:
    user_object = api.me()
#   print(json.dumps(user_object, indent=4, sort_keys=True))
    print(user_object.get('name'))

except Exception as e:
    print("api.me threw an Exception:")
    for arg in e.args:
        print(arg)
