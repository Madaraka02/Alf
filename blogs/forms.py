from django.forms import ModelForm
from .models import *


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'snippet',  'image']


class CommentForm(ModelForm):
    class Meta:
        model=Comment
        fields=['comment']        