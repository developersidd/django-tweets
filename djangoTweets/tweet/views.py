from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "tweet/index.html")

def tweet_details(request):
    return render(request, "tweet/tweet_details.html")
