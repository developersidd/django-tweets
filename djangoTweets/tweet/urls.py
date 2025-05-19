from django.urls import path
from . import views
urlpatterns = [
    path("", views.tweet_list, name="tweet_list"),
    path("result", views.searched_tweets, name="searched_tweets"),
    path("<int:tweet_id>/", views.tweet_details, name="tweet_details"),
    path("create/", views.tweet_create, name="tweet_create"),
    path("edit/<int:tweet_id>", views.tweet_edit, name="tweet_edit"),
    path("<int:tweet_id>/delete", views.tweet_delete, name="tweet_delete"),
    path("comment/<int:comment_id>/edit/", views.comment_edit, name="edit_comment"),
    path("comment/<int:comment_id>/delete/", views.comment_delete, name="delete_comment"),
    path("register", views.register_user, name="register"),
]
