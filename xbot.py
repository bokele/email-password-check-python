import tweepy
import time



consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.verify_credentials()
print (user.name) #prints your name.
print (user.screen_name)
print (user.followers_count)

search = "uvatechs"
numberOfTweets = 2

def limit_handle(cursor):
  while True:
    try:
      yield cursor.next()
    except tweepy.TooManyRequests:
      time.sleep(1000)


#Be nice to your followers. Follow everyone!
for follower in limit_handle(tweepy.Cursor(api.get_followers).items()):
  if follower.name == 'Usernamehere':
    print(follower.name)
    follower.follow()


# Be a narcisist and love your own tweets. or retweet anything with a keyword!
for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.favorite()
        print('Retweeted the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break