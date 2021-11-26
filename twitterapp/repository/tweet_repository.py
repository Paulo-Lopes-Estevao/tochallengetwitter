from typing import Type
from twitterapp.models import Tweet


class tweetRepository():

    def __init__(self, Tweet: Type[Tweet]):
        self.tweet = Tweet

    def findall_tweets(self) -> Tweet:
        return self.tweet.filter(state=True).values()

    def findbyid_tweets(self, id: int) -> Tweet:
        tweets = self.tweet.objects.filter(id=id)
        return tweets

    def create_tweet(self, **tweets) -> Tweet:
        tweet = self.tweet()
        tweet.user_id = tweets.get('user')
        tweet.description = tweets.get('description')
        tweet.midia = tweets.get('midia',None)
        tweet.emoji = tweets.get('emoji',None)
        tweet.gif = tweets.get('gif',None)
        result_tweet = tweet.save()
        return result_tweet

    def delete_tweet(self, id) -> Tweet:
        return self.tweet.objects.filter(id=id).update(state=False)