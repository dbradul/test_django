import os

from django.conf import settings
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm, CharField

from accounts.models import Profile


class AccountCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username']


class AccountUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class AccountProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'interests']
