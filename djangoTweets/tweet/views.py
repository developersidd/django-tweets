from django.shortcuts import render


# Create your views here.
def tweet_details(request):
    return render(request, "tweet/tweet_details.html")
