from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import Tweet
import random


def home_view(request, *args, **kwargs):
    # return HttpResponse("Home View")
    return render(request, 'pages/home.html', context={}, status=200)


def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweets_list = [{"id": x.id, "content": x.content, "likes": random.randint(0, 112)} for x in qs]

    data = {
        "isUser": False,
        "response": tweets_list
    }

    return JsonResponse(data)


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    """
    REST API VIEW
    Consumed by Javascript or Swift or Java/Ios/Swift/Android
    :return: json data
    """
    data = {
        "id": tweet_id,
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except Exception:
        data['message'] = "Not Found"
        status = 400

    return JsonResponse(data, status=status) # similar to json.dumps with content_type='application/json'