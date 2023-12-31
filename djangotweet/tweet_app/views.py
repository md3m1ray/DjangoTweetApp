from django.shortcuts import render, redirect
from . import models
from django.urls import reverse
from tweet_app.forms import AddTweetForm

# Create your views here.

def listtweet(request):
    all_tweets =models.Tweet.objects.all()
    tweet_dict = {'tweets' : all_tweets}
    return render(request, 'tweet_app/listtweet.html', context=tweet_dict)

def addtweet(request):
    if request.POST:
        nickname = request.POST['nickname']
        message = request.POST['message']
        models.Tweet.objects.create(nickname=nickname, message=message)
        return redirect(reverse('tweet_app:listtweet'))
    return render(request, 'tweet_app/addtweet.html')

def addtweetbyform(request):
    if request.method == 'POST':
        print(request.POST)
        return redirect(reverse('tweet_app:listtweet'))
    else:
        form = AddTweetForm()
        return render(request, 'tweet_app/addtweetbyform.html', context={'form':form})