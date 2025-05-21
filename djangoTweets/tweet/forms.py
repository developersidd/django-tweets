from django import forms
from .models import Tweet, Comment


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        # using list because using own custom form
        fields = ["text", "photo"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]

    comment = forms.CharField(
        widget=forms.Textarea(
            attrs={"placeholder": "Enter you comment", "class": "form-control"}
        )
    )
