from django.urls import path
from .views import tweet_details, home

urlpatterns = [
    path("", home, name="home"),
    path("<int:tweetId>/", tweet_details, name="tweet_details"),
]
