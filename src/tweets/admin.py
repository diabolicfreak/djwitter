from django.contrib import admin
from .models import Tweet
from .forms import TweetFormModel

class TweetModelAdmin(admin.ModelAdmin):
    form = TweetFormModel
    
admin.site.register(Tweet, TweetModelAdmin)