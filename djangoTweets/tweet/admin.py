from django.contrib import admin
from .models import Tweet, Comment

# Register your models here.


class TweetCommentInline(admin.TabularInline):
    model = Comment
    extra = 2


class TweetAdmin(admin.ModelAdmin):
    list_display = ("text", "user", "created_at")
    inlines = [TweetCommentInline]


admin.site.register(Tweet, TweetAdmin)
