from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    telefone = models.CharField(db_column='telefone', max_length=12, blank=True, null=True)
    state = models.BooleanField(default=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)


    REQUIRED_FIELDS = ('email',)
    def __str__(self):
        return self.username

class Tweet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, models.CASCADE, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    midia = models.TextField(blank=True, null=True)
    emoji = models.TextField(blank=True, null=True)
    gif = models.TextField(blank=True, null=True)
    reation = models.IntegerField(max_length=1,blank=True, null=True)
    state = models.BooleanField(default=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)


class Retweet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    tweet = models.ForeignKey(Tweet, models.CASCADE, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    midia = models.TextField(blank=True, null=True)
    emoji = models.TextField(blank=True, null=True)
    gif = models.TextField(blank=True, null=True)
    state = models.BooleanField(default=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)