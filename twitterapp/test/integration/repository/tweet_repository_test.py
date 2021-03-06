import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
import django

django.setup()
from django.core.management import call_command

import unittest

from twitterapp.repository.tweet_repository import tweetRepository
from twitterapp.usecase.tweet_usecase import tweetUsecase


class TweetRepositoryTestCase(unittest.TestCase):

    def setUp(self):
        self.tweet_usecase = tweetUsecase(tweetRepository=tweetRepository)

    def test_create_tweets(self):
        data_tweet = {"user":"ef5da2dc-3b46-4d30-92f2-154f6f75f1ad", "description": 'Olá primeiro tweets', 'midia': '/source/test.png'}
        tweet = self.tweet_usecase.addTweets(**data_tweet)
        self.assertGreaterEqual(len(tweet), 1, "tweets não publicada cadastrado")

    def test_deactivate_tweets(self):
        tweets = self.tweet_usecase.deletebyid_tweet("59b26050-cf1f-4ae6-a017-c95aa7108bc9")
        self.assertTrue(tweets,"tweets não removido")

    def test_likes_tweets(self):
        tweets = self.tweet_usecase.likes_in_tweets("59b26050-cf1f-4ae6-a017-c95aa7108bc9")
        self.assertTrue(tweets, "error in likes")


if __name__ == '__main__':
    unittest.main()
