from django.urls import path
from . import views

app_name = 'tweet_app'

urlpatterns = [
    path('addbyform', views.addtweetbyform, name='addtweetbyform'),
    path('add/', views.addtweet, name='addtweet'),
    path('', views.listtweet, name='listtweet'),

]