from django import forms
from .models import  Profile
from django.contrib.auth.models import User


# Update User Profile Form
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["avatar"]
