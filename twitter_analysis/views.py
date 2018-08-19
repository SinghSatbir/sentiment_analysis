from django.http import HttpResponse
from django.shortcuts import render
import tweepy

# Create your views here.
from django.template import loader
from twitter_analysis.forms import Form
from twitter_analysis.models import Word

def index(request):
    template = loader.get_template('index.html')
    context = {

    }
    return HttpResponse(template.render(context, request))

def form_view(request):
    template = loader.get_template('forms.html')
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

def result_view(request):
    template = loader.get_template('result.html')
    consumer_key = "6JMPol8gD9BuGUVKA5QQg5sBt"
    consumer_secret = "TQTuy8wYA9zH9qTYO7TXukUNHpA49Q4gMpuhyTfEHs7TTddBqH"
    access_token = "1029122549735673856-lXPMJE7Zr3uJ5kf4lUxVyMb65c0esk"
    access_token_secret = "xpswIoqLfJlgWivb9vh7DtzdiCPrc1Uh7oETF6jOwTnSp"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    positive=0
    negative=0
    neutral=0
    context={
        'keyword': Word.objects.last()
    }
    return HttpResponse(template.render(context, request))
