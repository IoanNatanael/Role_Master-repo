from django import forms
from .models import Post

from tinymce.widgets import TinyMCE


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'class': 'tinymce-editor'}))

    class Meta:
        model = Post
        fields = ['title', 'content']
