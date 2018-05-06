from django.shortcuts import render, get_object_or_404
from .models import Tweet
from django.views.generic import ListView, DetailView

def list_view(request):
    object_list = Tweet.objects.all()
    return render(request, 'tweets/list_view.html', {'object_list': object_list}) 

def detail_view(request, id=1):
    object = Tweet.objects.get(id=id)
    return render(request, 'tweets/detail_view.html', {'object': object}) 

class TweetListView(ListView):
    queryset = Tweet.objects.all()

class TweetDetailView(DetailView):
    # queryset = Tweet.objects.all()
    template_name = 'tweets/tweet_detail.html'
    def get_object(self):
        # return Tweet.objects.get(id=self.kwargs.get('pk'))
        return get_object_or_404(Tweet, pk=self.kwargs.get('pk'))