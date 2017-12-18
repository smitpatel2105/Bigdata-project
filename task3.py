import sys
import tweepy

# create class for get detail and for authenticat
consumer_key="u2iPpJv2YvCzIxWEQVUohx6UT" 
consumer_secret="E8A9xMnaGUwyoTJXgX5wwl0NCQbIogOEYUqyU1qmeyHjjajyiV"
access_key="923333025911463937-6txYTmayzCrxUqT2qpHbYswjNXnSQHn"
access_secret="vuXY1yciIfxz8dehd7XCALdEPcjRHpzTcda68ac65yHuW"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

#create class
class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
	#it will show all tweets which contain are word
        if 'are' in status.text.lower():
            print (status.text)

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True 

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True 

sapi = tweepy.streaming.Stream(auth, CustomStreamListener())   
#enter locatin in which location you want to search tweets 
sapi.filter(locations=[-122.75, 36.8, -121.75, 37.8])




# -122.75, 36.8, -121.75, 37.8
# 32, -5, 45, -7
# 5.0770049095, 47.2982950435, 15.0403900146, 54.9039819757
