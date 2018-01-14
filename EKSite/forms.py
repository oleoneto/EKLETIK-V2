from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

#_________________________________________



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


class MessageForm(forms.Form):
    class Meta:
        model = Message
        fields = ('sender', 'message', 'origin', 'subject')


#______________________________

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class EditProfileForm(UserChangeForm):
    template_name='/something/else'

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'
        )