from django.conf.urls import url, include
from .views import TweetListAPIView, TweetCreateAPIView

urlpatterns = [
    url(r'^$', TweetListAPIView.as_view(), name='list'),
    url(r'^create$', TweetCreateAPIView.as_view(), name='list')    
]
