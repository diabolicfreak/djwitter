from django.db import models
from django.urls import reverse
from django.conf import settings

class Tweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.CharField(max_length=140)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
        
    def get_absolute_url(self):
        return reverse('tweet:detail', kwargs={'pk': self.pk})