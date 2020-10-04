from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm


class AccountCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name', 'last_name']


class AccountUpdateForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields = ['username', 'first_name', 'last_name', 'email']