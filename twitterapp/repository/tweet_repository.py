
from typing import Type
from twitterapp.models import Tweet


class tweetRepository():

    def __init__(self,Tweet: Type[Tweet]):
        self.tweet = Tweet

    def findall_tweets(self):
        return self.tweet

    def findbyid_tweets(self,id: int):
        tweets = self.tweet.objects.filter(id=id)
        return tweets


    def create_tweet(self, **tweet):
        self.tweet.user_id = tweet.get('user_id')
        self.tweet.description = tweet.get('description')
        self.tweet.midia = tweet.get('midia')
        self.tweet.emoji = tweet.get('emoji')
        self.tweet.gif = tweet.get('gif')
        self.tweet.reation = tweet.get('reation')
        return self.tweet.save()

    def delete_tweet(self, id):
        self.tweet.objects.filter(id=id).update(state=False)