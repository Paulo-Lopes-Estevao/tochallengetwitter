from typing import Type
from twitterapp.models import Tweet as TwitterModel

class Tweet:


    def addTweets(self,**tweet):
        try:
            return tweet
        except Exception as e:
            raise e

    def addRetweet(self,**tweet):
        try:
            return tweet
        except Exception as e:
            raise e

    def reationTweets(self,tweet: Type[TwitterModel]):
        try:
            reacted = tweet.values()[0].get("reation")
            if reacted == 0 or reacted == None:
                return 1
            return 0
        except Exception as e:
            raise e