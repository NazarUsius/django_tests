from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import User, Post


class AuthorPostsForm(forms.Form):
    author = forms.ModelChoiceField(queryset=User.objects.all(), required=False)

