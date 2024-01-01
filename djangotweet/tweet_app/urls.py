from django.urls import path
from . import views

app_name = 'tweet_app'

urlpatterns = [
    path('addmodelform', views.addtweetmodelform, name='addtweetmodelform'),
    path('addbyform', views.addtweetbyform, name='addtweetbyform'),
    path('add/', views.addtweet, name='addtweet'),
    path('', views.listtweet, name='listtweet'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('delete_tweet/<int:id>', views.delete_tweet, name='delete_tweet')
]