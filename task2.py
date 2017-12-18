#import tweepy
import tweepy

#authentication for connect to tweepy. we want 4 keys for that
consumer_key= 'u2iPpJv2YvCzIxWEQVUohx6UT'
consumer_secret= 'E8A9xMnaGUwyoTJXgX5wwl0NCQbIogOEYUqyU1qmeyHjjajyiV'
access_token= '923333025911463937-6txYTmayzCrxUqT2qpHbYswjNXnSQHn'
access_token_secret= 'vuXY1yciIfxz8dehd7XCALdEPcjRHpzTcda68ac65yHuW'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
    
#get user name
user = api.get_user(screen_name='@vabhishek990')

# loop for print friend list by friend list
print ("*******Retreiving friends for : ", user.screen_name," ********")
for friend in user.friends():
    print (friend.screen_name)

# loop for print friend list by followers list
print ("*******Retreiving followers for : ", user.screen_name," ********")
for followers in user.followers():
    print (followers.screen_name)

