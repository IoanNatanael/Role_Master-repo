from django import forms
from .models import InfoModel


class InfoPostForm(forms.ModelForm):
    class Meta:
        model = InfoModel
        fields = ['title', 'content']
