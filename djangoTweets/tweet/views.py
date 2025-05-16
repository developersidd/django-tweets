from django.shortcuts import render
from .models import Tweet
from django.shortcuts import get_object_or_404, redirect
from .forms import TweetForm


# Create your views here.
def home(request):
    return render(request, "tweet/index.html")


# create tweet
def tweet_create(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request
        form = TweetForm(request.POST, request.FILES)
        # check whether it's valid
        if form.is_valid():
            # first save the form
            # Don't save the form in DB now, but just save the form
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect("tweet_list")

    else:
        form = TweetForm
    return render(request, "tweet/tweet_form.html", {"form": form})


# Edit Tweet
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            form.save()
            return redirect("tweet_list")
    else:
        form = TweetForm(instance=tweet)
    return render(request, "tweet/tweet_form.html", {"form": form})


# delete tweet
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == "POST":
        tweet.delete()
        return redirect("tweet_list")
    return render(request, "tweet/tweet_confirm_delete.html", {"tweet": tweet})


# get Tweet list
def tweet_list(request):
    tweets = Tweet.objects.all().order_by("-created_at")
    return render(request, "tweet/tweet_list.html", {"tweets": tweets})


def tweet_details(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    return render(request, "tweet/tweet/tweet_details.html", {"tweet": tweet})
