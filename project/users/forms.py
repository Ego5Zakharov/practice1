from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UsernameField
from django.contrib.auth.views import LoginView

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'fio', 'gender', 'birth_date', 'groups')


class AuthenticationForm(forms.Form):
    model = CustomUser
    fields = ('username','fio','gender','birth_date','groups','money')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username','fio','gender','birth_date','groups','money')
