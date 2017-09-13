from django import forms
from .models import *

class DocForm(forms.ModelForm):
    class Meta:
        model = Doc
        fields = ('title', 'author', 'content')


# Contact Form
class ContactForm(forms.Form):
    contact_firstname = forms.CharField(required=True)
    contact_lastname  = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
