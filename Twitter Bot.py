import tweepy
import time

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print (user.name) #prints name
print (user.screen_name) #prints screen name
print (user.followers_count) #prints follower count

search = "python"
numberOfTweets = 2

def limit_handle(cursor):
  while True:
    try:
      yield cursor.next()
    except tweepy.RateLimitError:
      time.sleep(1000)

#Follow back users with greater than 100 followers
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
  if follower.followers_count > 100:
    print(follower.name)
    follower.follow()


#Favorites tweet with keyword 'Python' 
for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.favorite()
        print('Retweeted the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break