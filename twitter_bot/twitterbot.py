import tweepy
import time


consumer_key = 'IlKZzpEIxRbqkO2dgEMuodw0f'
consumer_secret = '1L9qbhHeLFA8JFw9e3fWwN5osr5Au6pf9QWGg4cUSPh5z3EDZM'
access_token = '2313277181-b1fDLk3txd7u6PbHYhQLB4yIvwgXiKDl2Yc81rZ'
access_token_secret = 'zPzJQfYZlNvgD1LGLJnr1UDMPIx9cQh6detDO8LWEUgW6'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me()

search_string = 'python'
numberOfTweets = 2


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
    try:
        tweet.favorite()
        print('liked this tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

