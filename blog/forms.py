from django import forms
from django.forms import ModelForm

from .models import Post

class CreatePost(ModelForm):
    class Meta:
        model = Post
        fields = ['postName','postDescript']
