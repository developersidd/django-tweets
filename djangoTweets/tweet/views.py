from django.shortcuts import render
from .models import Tweet, Comment
from django.shortcuts import get_object_or_404, redirect
from .forms import TweetForm, UserRegistrationForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db.models import Q
from django.http import HttpResponseForbidden


# Create your views here.
def home(request):
    return render(request, "tweet/index.html")


# create tweet
@login_required
def tweet_create(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request
        form = TweetForm(request.POST, request.FILES)
        # check whether it's valid
        if form.is_valid():
            # Get a Tweet instance but don't save it yet
            tweet = form.save(commit=False)
            # Set additional data not in the form
            tweet.user = request.user
            tweet.save()
            return redirect("tweet_list")

    else:
        form = TweetForm
    return render(request, "tweet/tweet_form.html", {"form": form})


# Edit Tweet
@login_required
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
@login_required
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


# get tweets search result
def searched_tweets(request):
    search = request.GET.get("search")
    print("🐍 File: tweet/views.py | Line: 69 | searched_tweets ~ search", search)
    tweets = Tweet.objects.filter(Q(text__icontains=search))
    print("🐍 File: tweet/views.py | Line: 70 | searched_tweets ~ tweets", tweets)
    return render(request, "tweet/searched_tweets.html", {"tweets": tweets})


# get tweet details
def tweet_details(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    # Add comments in tweet
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.tweet = tweet
            comment.user = request.user
            form.save()
            return redirect("tweet_details", tweet_id=tweet.id)
    else:
        form = CommentForm()

    return render(
        request, "tweet/tweet_details.html", {"tweet": tweet, "comment_form": form}
    )


# Edit Comment
@login_required
def comment_edit(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id, user=request.user)
    if request.user != comment.user:
        return HttpResponseForbidden("You are not allowed to edit this comment.")
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect("tweet_details", tweet_id=comment.tweet.id)

    else:
        form = CommentForm(instance=comment)
    return render(
        request, "tweet/edit_comment.html", {"form": form, "comment": comment}
    )


# Delete comment
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id, user=request.user)
    if request.user != comment.user:
        return HttpResponseForbidden("You are not allowed to delete this comment.")
    comment.delete()
    return redirect("tweet_details", tweet_id=comment.tweet.id)


# register user
def register_user(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            form.save()
            login(request, user=user)
            return redirect("tweet_list")

    else:
        form = UserRegistrationForm()

    return render(request, "registration/register.html", {"form": form})
