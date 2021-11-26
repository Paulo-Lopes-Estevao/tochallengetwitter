from typing import Type
from twitterapp.entities.tweet import Tweet
from twitterapp.models import Retweet as retweetModel
from twitterapp.repository.retweet_repository import retweetRepository


class retweetUsecase:

    def __init__(self, retweetRepository: Type[retweetRepository]):
        self.retweet_repository = retweetRepository(Retweet=retweetModel)

    def getRetweets(self) -> retweetModel:
        return self.retweet_repository.findall_retweets()

    def getByIdRetweets(self, id) -> retweetModel:
        return self.retweet_repository.findbyid_retweets(id)

    def addRetweets(self, **retweet) -> retweetModel:
        retweets = Tweet().addRetweets(**retweet)
        self.retweet_repository.create_retweet(**retweets)
        return retweets

    def likes_in_retweets(self, id):
        retweets = self.retweet_repository.findbyid_retweets(id)
        like_react = Tweet().reationTweets(retweets)
        if retweets.exists():
            return self.retweet_repository.reation_retweets(id, like_react)

    def deletebyid_retweet(self, id) -> retweetModel:
        return self.retweet_repository.delete_retweet(id)
