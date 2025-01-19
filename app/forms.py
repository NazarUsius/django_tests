from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class AuthorPostsForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput())