# Set dependancies
import tweepy
import json

# Set Twitter credentials.
consumer_key="YhICRiL9rXjMj5gC74v8Bi7Wa"
consumer_secret="RhPW6tVd7j8GC6wP9byWE7hdvAxmo6s15H6LappofOm5iByF7U"

access_token="973957423152095232-BlngqUDT7UhLsl3I6mSW9YXNkL5401H"
access_token_secret="b20uzJQa76vxhzdzmdv6QVVH1Dt7BDT5BezJiKDkgoxWO"

# Set Authentication Handler
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

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
