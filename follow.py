import tweepy
import time

auth = tweepy.OAuthHandler('WoV8KmX9cFAcyACsLP0JdaniF','Y1Gs0cuzrYUoYxURtAb9DYa3VU93ZwcuYt3Ns68wjvKY6FJuMb')
auth.set_access_token('1221811184741036032-6CIGhxLCxaoJLsYXFYWidGEhWVsi0B','tvL0UQ1W7kKsvr2WjGg6jUnS82CWDjw3tlLk8TH3fKE4b')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()

nrFollowers = 5

for follower in tweepy.Cursor(api.followers).items(nrFollowers):
    try:
        print('Followed Back')
        follower.follow()
        time.sleep(360)
    except tweepy.TweepError as errorCode:
        print(errorCode.reason)
    except StopIteration:
        break