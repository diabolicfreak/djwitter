from django import forms
from .models import Tweet

class TweetFormModel(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = [
            'user',
            'content',
        ]

    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data.get('content')
        return content
