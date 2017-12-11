from tweetfeels import TweetFeels
from threading import Thread
import time

consumer_key = 'bwFAEEaVbmXe5yvCQbRtrRKpH'
consumer_secret = 'ABsNsIpIQnXq2s3QOmKgWyXw5C2cmloX6vwel2cMJSqXTlh17b'
access_token = '4619664500-gMgtDANkMqq7iaqJ8i2o4sIEl8ACRt8fMi3Ygh9'
access_token_secret = 'CBEPCPjisrazBOtidNZSTdK3y6v710Htn32l3Vby0uMZl'
login = [consumer_key, consumer_secret, access_token, access_token_secret]


feels = TweetFeels(login, tracking=['bitcoin'])

# trump_feels.start(10)
# print(trump_feels.sentiment.value)


def print_feels(seconds=10):
	while go_on:
		time.sleep(seconds)
		print(f'[{time.ctime()}] Sentiment Score: {feels.sentiment.value}')


go_on = True
t = Thread(target=print_feels)
feels.start()
t.start()