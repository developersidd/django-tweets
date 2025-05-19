from django.urls import path
from .views import (
    tweet_details,
    tweet_list,
    tweet_create,
    tweet_edit,
    tweet_delete,
    register_user,
    searched_tweets,
)

urlpatterns = [
    path("", tweet_list, name="tweet_list"),
    path("result", searched_tweets, name="searched_tweets"),
    path("<int:tweet_id>/", tweet_details, name="tweet_details"),
    path("create/", tweet_create, name="tweet_create"),
    path("<int:tweet_id>/edit/", tweet_edit, name="tweet_edit"),
    path("<int:tweet_id>/delete", tweet_delete, name="tweet_delete"),
    path("register", register_user, name="register"),
]
