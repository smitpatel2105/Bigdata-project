#import all file which we want for get detail of user detail
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import urllib
import time
import subprocess

#authentication for connect to tweepy. we want 4 keys for that
CONSUMER_KEY = 'u2iPpJv2YvCzIxWEQVUohx6UT'
CONSUMER_SECRET = 'E8A9xMnaGUwyoTJXgX5wwl0NCQbIogOEYUqyU1qmeyHjjajyiV'
ACCESS_KEY = '923333025911463937-6txYTmayzCrxUqT2qpHbYswjNXnSQHn'
ACCESS_SECRET = 'vuXY1yciIfxz8dehd7XCALdEPcjRHpzTcda68ac65yHuW'

# create class for get detail and for authenticat
class TweetListener(StreamListener):
   
    def on_data(self, data):
        print (""+data)        
        return(True)
        

    def on_error(self, status):
       print (""+status)

auth = OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
api = tweepy.API(auth)

auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
twitterStream = Stream(auth,TweetListener())

#get user name
user = api.get_user(screen_name='@vabhishek990')

friends_count= 0

#loop for count totral friend
for friend in user.friends():    
    friends_count= friends_count+ 1

#print all detail for any user
print ('Screen Name: '+user.screen_name)
print ('Followers: ',user.followers_count)
print ('Friends: ',friends_count)
print ('Statuses: ', user.statuses_count)
print ('Url :',user.url)
print ('Description: '+user.description)




