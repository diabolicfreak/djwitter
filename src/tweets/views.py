from django.shortcuts import render, get_object_or_404
from .models import Tweet
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import TweetFormModel
from django.forms.utils import ErrorList
from django import forms
from django.db.models import Q
from .mixins import UserOwnerMixin
from django.urls import reverse_lazy

def list_view(request):
    object_list = Tweet.objects.all()
    return render(request, 'tweets/list_view.html', {'object_list': object_list}) 

def detail_view(request, id=1):
    object = Tweet.objects.get(id=id)
    return render(request, 'tweets/detail_view.html', {'object': object}) 

class TweetListView(ListView):
    
    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all()
        print(self.request.GET)
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                    Q(content__icontains=query) |
                    Q(user__username__icontains=query)
                    )
        return qs

    def get_context_data(self):
        context = super().get_context_data()
        context['form_content'] = TweetFormModel()
        context['submit_url'] = reverse_lazy('tweet:create')
        context['btn_value'] = "Submit"
        return context
            
class TweetDetailView(DetailView):
    # queryset = Tweet.objects.all()
    template_name = 'tweets/tweet_detail.html'
    def get_object(self):
        # return Tweet.objects.get(id=self.kwargs.get('pk'))
        return get_object_or_404(Tweet, pk=self.kwargs.get('pk'))
    
class TweetCreateView(CreateView):
    form_class = TweetFormModel
    template_name = 'tweets/tweet_create.html'
    # success_url = '/tweets'

    def form_valid(self, form):
        if self.request.user.is_authenticated():
            form.instance.user = self.request.user
            return super().form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User must be logged in"])
            return self.form_invalid(form)

class TweetUpdateView(UserOwnerMixin, UpdateView):
    form_class = TweetFormModel
    template_name = 'tweets/tweet_update.html'
    queryset = Tweet.objects.all()
    success_url = '/tweets'