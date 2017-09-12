from django import forms
from .models import *

class DocForm(forms.ModelForm):
    class Meta:
        model = Doc
        fields = ('title', 'author', 'content')