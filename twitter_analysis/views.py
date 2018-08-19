from django.http import HttpResponse
from django.shortcuts import render
import tweepy

# Create your views here.


def index(request):
    consumer_key = "6JMPol8gD9BuGUVKA5QQg5sBt"
    consumer_secret = "TQTuy8wYA9zH9qTYO7TXukUNHpA49Q4gMpuhyTfEHs7TTddBqH"
    access_token = "1029122549735673856-lXPMJE7Zr3uJ5kf4lUxVyMb65c0esk"
    access_token_secret = "xpswIoqLfJlgWivb9vh7DtzdiCPrc1Uh7oETF6jOwTnSp"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

