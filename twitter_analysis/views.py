from django.http import HttpResponse
from django.shortcuts import render
import tweepy

# Create your views here.
from django.template import loader
from twitter_analysis.forms import Form


def index(request):
    template = loader.get_template('index.html')
    context = {

    }
    return HttpResponse(template.render(context, request))

def form_view(request):
    template = loader.get_template('')
    form_object = Form()
    if request.method == 'POST':
        form_object = Form(request.POST)
        if form_object.is_valid():
            form_object.save(commit=True)
            return index(request)
    context = {
        'form_full': form_object
    }
    return HttpResponse(template.render(context, request))
    # consumer_key = "6JMPol8gD9BuGUVKA5QQg5sBt"
    # consumer_secret = "TQTuy8wYA9zH9qTYO7TXukUNHpA49Q4gMpuhyTfEHs7TTddBqH"
    # access_token = "1029122549735673856-lXPMJE7Zr3uJ5kf4lUxVyMb65c0esk"
    # access_token_secret = "xpswIoqLfJlgWivb9vh7DtzdiCPrc1Uh7oETF6jOwTnSp"
    # auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # auth.set_access_token(access_token, access_token_secret)

