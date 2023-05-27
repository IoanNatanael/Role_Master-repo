from django import forms
from tinymce.widgets import TinyMCE
from .models import Post


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'class': 'tinymce-editor'}))

    class Meta:
        model = Post
        fields = ['title', 'content']
