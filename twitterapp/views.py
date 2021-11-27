import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.views import View
from twitterapp.models import User
from twitterapp.usecase.interactor.user_interactor import userInteractor
from twitterapp.repository.user_repository import userRepository
from twitterapp.repository.tweet_repository import tweetRepository
from twitterapp.usecase.tweet_usecase import tweetUsecase
from twitterapp.repository.retweet_repository import retweetRepository
from twitterapp.usecase.retweet_usecase import retweetUsecase

user_interactor = userInteractor(userRepository=userRepository)
retweet_usecase = retweetUsecase(retweetRepository=retweetRepository)
tweet_usecase = tweetUsecase(tweetRepository=tweetRepository)


def WelcomeView(request):
    if request.method == 'GET':
        return JsonResponse({"Bem-vindo"},status=200)

# Create your views here.
def UsersView(request):
    if request.method == 'GET':
        data =list(user_interactor.getUsers())
        new_dict = {}
        for item in data:
            id =str(item["id"])
            new_dict[id] = item
        return JsonResponse(new_dict, status=200, content_type="application/json")
    elif request.method == 'POST':
        pass


class RetweetsView(View):
    def post(self, request, *args, **kwargs):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        retweet_usecase.addRetweets(**body)
        data = {"message": "retweet cadastrado", "data": body, "status": 201}
        return JsonResponse(data, status=201)



def TweetsLikeView(request, *args, **kwargs):
    if request.method == 'PUT':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        retweet_usecase.likes_in_retweets(body.get("id"))
        return JsonResponse({"message": "reacted", "status": 200}, status=200)


def RetweetsFeedView(request, *args, **kwargs):
    if request.method == 'GET':
        data = list(retweet_usecase.getRetweets())
        new_dict = {}
        for item in data:
            id = str(item["id"])
            new_dict[id] = item
        return JsonResponse(new_dict, status=200, content_type="application/json")

def RetweetsDeleteView(request, id, *args, **kwargs):
    if request.method == 'GET':
        try:
            retweet = retweet_usecase.deletebyid_retweet(id)
            if retweet == 0:
                return JsonResponse({"message": "id tweet não encontrado", "status": 404}, status=404)
            return JsonResponse({"message": "retweet deletado", "status": 200}, status=200)
        except Exception as e:
            return JsonResponse({"message": "id tweet não encontrado", "status": 404}, status=404)



def TweetsFeedView(request, *args, **kwargs):
    if request.method == 'GET':
        data = list(tweet_usecase.getTweets())
        new_dict = {}
        for item in data:
            id = str(item["id"])
            new_dict[id] = item
        return JsonResponse(new_dict, status=200, content_type="application/json")

def TweetsCreateView(request, *args, **kwargs):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        tweet_usecase.addTweets(**body)
        data = {"message": "tweet cadastrado", "data": body, "status": 201}
        return JsonResponse(data, status=201)

def TweetsLikeView(request, *args, **kwargs):
    if request.method == 'PUT':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        tweet_usecase.likes_in_tweets(body.get("id"))
        return JsonResponse({"message": "reacted", "status": 200}, status=200)


def TweetsDeleteView(request, id, *args, **kwargs):
    if request.method == 'GET':
        tweet = tweet_usecase.deletebyid_tweet(id)
        if tweet == 0:
            return JsonResponse({"message": "id tweet não encontrado", "status": 404}, status=404)
        return JsonResponse({"message": "tweet deletado", "status": 200}, status=200)
