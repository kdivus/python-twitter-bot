import tweepy
import time 

auth = tweepy.OAuthHandler('your api key', 'api secret')
auth.set_access_token('your access token', 'your access token')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = 'your search term'
nrTweets = 100

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        tweet.favorite()
        #tweet.retweet()
        print('Tweet Liked!')
        print('Sleep 2 secs...')
        time.sleep(2)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break        


""" print(user)
print(user.screen_name) 

for follower in tweepy.Cursor(api.followers).items():
    #print(follower.name) """