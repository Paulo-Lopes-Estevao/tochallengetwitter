from typing import Type
from twitterapp.entities.tweet import Tweet
from twitterapp.models import Tweet as tweetModel
from twitterapp.repository.tweet_repository import tweetRepository


class tweetUsecase:

    def __init__(self, tweetRepository: Type[tweetRepository]):
        self.tweet_repository = tweetRepository(Tweet=tweetModel)

    def getTweets(self) -> tweetModel:
        return self.tweet_repository.findall_tweets()

    def getByIdTweets(self, id) -> tweetModel:
        return self.tweet_repository.findbyid_tweets(id)

    def addTweets(self, **tweet) -> tweetModel:
        tweets = Tweet().addTweets(**tweet)
        self.tweet_repository.create_tweet(**tweets)
        return tweets

    def likes_in_tweets(self, id):
        tweets = self.tweet_repository.findbyid_tweets(id)
        like_react = Tweet().reationTweets(tweets)
        if tweets.exists():
            return self.tweet_repository.reation_tweets(id, like_react)

    def deletebyid_tweet(self, id) -> tweetModel:
        return self.tweet_repository.delete_tweet(id)
