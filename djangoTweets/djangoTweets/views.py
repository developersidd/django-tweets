from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegistrationForm


def home(request):
    return render(request, "index.html")


def login_page(request):
    if request.user.is_authenticated:
        return redirect("tweet_list")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(
            "🐍 File: djangoTweets/views.py | Line: 15 | login_page ~ username, password",
            username,
            password,
        )

        try:
            user = User.objects.get(username=username)
            print("🐍 File: djangoTweets/views.py | Line: 20 | login_page ~ user", user)

        except:
            messages.error("User not found!")

        user = authenticate(request, username=username, password=password)
        print(
            "🐍 File: djangoTweets/views.py | Line: 26 | login_page ~ authticated user",
            user,
        )

        if user is not None:
            login(request, user)
            return redirect("tweet_list")
        else:
            messages.error("Username OR password does not exist ")
    return render(request, "login.html")


# register user
def register_page(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            print(
                "🐍 File: djangoTweets/views.py | Line: 51 | register_page ~ user", user
            )
            # user.set_password(form.cleaned_data["password1"])
            form.save()
            login(request, user=user)
            return redirect("tweet_list")
        else:
            messages.error(request, "An error occurred during registration")

    else:
        form = UserRegistrationForm()

    return render(request, "register.html", {"form": form})


def logoutUser(request):
    logout(request)
    return redirect("tweet_list")
