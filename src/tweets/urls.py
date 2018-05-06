from django.conf.urls import url, include
from .views import TweetListView, TweetDetailView

urlpatterns = [
    url(r'^$', TweetListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', TweetDetailView.as_view(), name='detail'),
    # url(r'^$', list_view, name='list'),  
]