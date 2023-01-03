from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'password1', 'password2']


class UpdateUserForm(ModelForm):
    column1 = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'column1']
