"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from twitterapp.views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('/', csrf_exempt(WelcomeView)),

    path('v1/users', csrf_exempt(UsersView)),

    path('v1/retweets', csrf_exempt(RetweetsFeedView)),
    path('v1/retweets', csrf_exempt(RetweetsView.as_view())),
    path('v1/retweets/like', csrf_exempt(TweetsLikeView)),
    path('v1/retweets/<str:id>/', csrf_exempt(RetweetsDeleteView)),

    path('v1/tweets', csrf_exempt(TweetsFeedView)),
    path('v1/tweets', csrf_exempt(TweetsCreateView)),
    path('v1/tweets/like', csrf_exempt(TweetsLikeView)),
    path('v1/tweets/<str:id>/', csrf_exempt(TweetsDeleteView)),
]
