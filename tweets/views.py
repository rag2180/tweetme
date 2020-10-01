from django.shortcuts import render
from django.http import HttpResponse
from .models import Tweet


def home_view(request, *args, **kwargs):
    return HttpResponse("Home View")


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    obj = Tweet.objects.get(id=tweet_id)
    return HttpResponse("Home {}  - {}".format(tweet_id, obj.content))