from typing import Type
from twitterapp.models import Retweet


class retweetRepository():

    def __init__(self, Retweet: Type[Retweet]):
        self.retweet = Retweet

    def findall_retweets(self) -> Retweet:
        return self.retweet.filter(state=True).values()

    def findbyid_retweets(self, id) -> Retweet:
        retweets = self.retweet.objects.filter(id=id)
        return retweets

    def create_retweet(self, **retweets) -> Retweet:
        retweet = self.retweet()
        retweet.tweet_id = retweets.get('tweet')
        retweet.description = retweets.get('description',None)
        retweet.midia = retweets.get('midia',None)
        retweet.emoji = retweets.get('emoji',None)
        retweet.gif = retweets.get('gif',None)
        result_retweet = retweet.save()
        return result_retweet

    def reation_retweets(self, id, reacted)->Retweet:
        return self.retweet.objects.filter(id=id).update(reation=reacted)

    def delete_retweet(self, id) -> Retweet:
        return self.retweet.objects.filter(id=id).update(state=False)