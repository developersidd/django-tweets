from django.db import models
from django.contrib.auth.models import User


# User Profile Model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        default="default_avatar.png",
        upload_to="avatars/",
    )
    bio = models.TextField(max_length=300)

    def __str__(self):
        return self.user.username
