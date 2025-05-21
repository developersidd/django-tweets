from django.shortcuts import render
from django.shortcuts import redirect, HttpResponse
from .forms import ProfileUpdateForm
from django.contrib.auth.decorators import login_required


def home(request):
    return HttpResponse("Hello")


# Profile
@login_required(login_url="login")
def profile(request):
    if request.method == "POST":
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if profile_form.is_valid():
            profile_form.save()
            return redirect("profile")
    else:
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, "users/profile.html", {"profile_form": profile_form})
