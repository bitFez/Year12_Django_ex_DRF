from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from . models import Reviews

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'password1', 'password2']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['title', 'body', 'imdb_ref', 'image', 'criticR']
