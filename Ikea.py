import tweepy
import csv
from csv import writer

#!/usr/bin/python
from tweepy import Stream, OAuthHandler
from tweepy.streaming import StreamListener


#cambiar a listener en lugar de setramlistener. due to tweepy version

#from progressbar import ProgressBar, Percentage, Bar #pip install progressbar2
import json
import sys
import time
import datetime
#import math
#from IPython.html.widgets import FloatProgress
#from IPython.display import display

#Twitter app information
# import twitter_keys
# consumer_secret, consumer_key, access_token, access_token_secret = twitter_keys.get_twitter_keys()


#Twitter app information
consumer_key = 'tPIOhBqyT0oIRtKYfNrkSb1ix'
consumer_secret = '47gjIAOaRLwJ2n0ai5uinY6IPDAhC5mrxq2kWxmY4Ok7lklGBs'
access_token = '2784593887-aGpyYX3Fl6xsy9U73xsciSHXsaUinwh6dzwp1Ud'
access_token_secret = 'uwS3bz7L5hsbNBg4gjzUp0m6RYUKBlIGIfLd7aK2PloCq'


data_track = ['ikea']

#The number of tweets we want to get
max_tweets = 5
#hours
timeout = 10
data_storage = data_track[0]

print (data_storage)

st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H%M%S')
file_name = data_storage + st + '.csv'
file_name


timeout = 1 * 60 * timeout
timeout = time.time() + timeout
#file_load = FloatProgress(min=0, max=100)

#Get the OAuth token
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
api

datetime.datetime.utcnow().strftime("%a %b %d %H:%M:%S %Z %Y")

#Create the listener class that receives and saves tweets
class listener(StreamListener):
    #On init, set the counter to zero and create a progress bar
    def __init__(self, api=None):
        self.num_tweets = 0.0
        #self.pbar = ProgressBar(widgets=[Percentage(), Bar()], maxval=max_tweets).start()
        
    #When data is received, do this
    def on_data(self, data):
        #Append the tweet to the 'tweets.txt' file        
        #with open(file_name, 'a') as tweet_file:
        with open(file_name, 'a', newline='', encoding='utf-8') as tweet_file:
            
            csv = writer(tweet_file, lineterminator = '\n')
            #c = csv.writer(open("Myfile.csv", 'w',  newline='', encoding='utf-8'))
            while self.num_tweets < max_tweets:               
                tweet = json.loads(data)
                
                # print(data)
                # disable this line once your testing is done
                print (tweet)
                
                # Pull out as any fields as you can. Examples given in the below
                row = (                   
                    tweet['id_str'],
                    tweet['created_at'],
                    tweet['text'],
                    tweet['lang'],
                    tweet['source'],
                    tweet['user']['screen_name'],
                    tweet['user']['lang'],
                    tweet['user']['description'],
                    tweet['user']['location'],
                    tweet['retweet_count']
                    
                    #Replace XXj with the real names
                    #tweet['XX1'],
                    #tweet['XX2']
                )

                values = row
                
                csv.writerow(values)
                self.num_tweets += 1
                if self.num_tweets == max_tweets:
                    #file_load.value = 0
                    tweet_file.close()
                    return False
                else: 
                    #end loop, maximum reached
                    return True
        #return False
    #Handle any errors that may occur
    def on_error(self, status):
        print (status)
while time.time() < timeout:
    st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H%M%S')
    file_name = data_storage + st + '.csv'
    #Prevent error 420: Connection overlap
    time.sleep(2)
    #Use the listener class for stream processing
    twitterStream = Stream(auth, listener())
    #Filter for these topics
    twitterStream.filter(track=data_track)
    if time.time() >= timeout:
        print ('close')
        #break