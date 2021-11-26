import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
import django

django.setup()
from django.core.management import call_command

import unittest

from twitterapp.repository.retweet_repository import retweetRepository
from twitterapp.usecase.retweet_usecase import retweetUsecase


class RetweetRepositoryTestCase(unittest.TestCase):

    def setUp(self):
        self.retweet_usecase = retweetUsecase(retweetRepository=retweetRepository)

    def test_create_retweets(self):
        data_retweet = {"tweet": "59b26050-cf1f-4ae6-a017-c95aa7108bc9", "description": 'Olá Retweets'}
        retweet = self.retweet_usecase.addRetweets(**data_retweet)
        self.assertGreaterEqual(len(retweet), 1, "retweets não publicada cadastrado")

    def test_deactivate_retweets(self):
        retweets = self.retweet_usecase.deletebyid_retweet("59b26050-cf1f-4ae6-a017-c95aa7108bc9")
        self.assertTrue(retweets, "retweets não removido")

    def test_likes_retweets(self):
        retweets = self.retweet_usecase.likes_in_retweets("7b0c72bb-419a-40b6-b4d7-ddab519722c3")
        self.assertTrue(retweets, "error in likes retweet")


if __name__ == '__main__':
    unittest.main()
