from django import forms

from .models import Blog

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            'title',
            'text',
            'pub_date',
            'category',
        ]