
# coding: utf-8

# In[ ]:


# Obtaining credentials.
from set_tweepy_context import api

# Dependencies
import tweepy
import json
import time
# print(json.dumps(homer, sort_keys=True, indent=4, separators=(',', ': ')))


# In[ ]:


# Delete the last twenty entries to avoid duplicate status messages.
def gosher():
    list_status = api.home_timeline()

    for status_entry in list_status:
        status_id = status_entry.get('id')
        status_text = status_entry.get('text')
        if status_text.startswith("Can't stop."):
            try:
                api.destroy_status(status_id)   
            except:
                print("Could not destroy", status_text)
                pass  


# In[ ]:


# Create a function that tweets
def TweetOut(tweet_number):
    
    tweet_str = "Can't stop. Won't stop. Chatting! This is Tweet {}.".format(tweet_number)
        
    try:
        api.update_status(tweet_str)
#         print("Added", str(tweet_number))

    except tweepy.TweepError as e:
        for arg in e.args:
            if arg[0].get('message') == "Status is a duplicate.":
                gosher()
                time.sleep(5)
                TweetOut(tweet_number)
    


# In[ ]:


# Infinitely loop
# while(counter < 10):
# Create a function that calls the TweetOut function every minute
counter = 0

while(True):

    # Call the TweetQuotes function and specify the tweet number
    TweetOut(counter)

    # Once tweeted, wait 60 seconds before doing anything else
    time.sleep(60)

    # Add 1 to the counter prior to re-running the loop
    counter += 1

