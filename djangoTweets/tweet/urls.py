from django.urls import path
from .views import tweet_details

urlpatterns = [path("", tweet_details, name="tweet_details")]
