from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Tweet Model
class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=240)
    photo = models.ImageField(upload_to="tweets/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.text[:10]}"


# Tweet Comments
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    tweet = models.ForeignKey(Tweet, related_name="comments", on_delete=models.CASCADE)
    comment = models.TextField(max_length=200)
    added_at = models.DateTimeField(default=timezone.now)
