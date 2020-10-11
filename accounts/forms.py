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


    # def save(self, commit=True):
    #     from PIL import Image
    #
    #
    #
    #     result =  super().save(commit)
    #
    #     # image = self.cleaned_data['image'].image
    #     basewidth = 300
    #     # img = Image.open(os.path.join(settings.BASE_DIR, 'media/', 'default.jpg'))
    #     img = Image.open(self.instance.image.file)
    #     wpercent = (basewidth / float(img.size[0]))
    #     hsize = int((float(img.size[1]) * float(wpercent)))
    #     img.resize((basewidth, hsize), Image.ANTIALIAS)
    #     img.thumbnail((basewidth, hsize), Image.ANTIALIAS)
    #     img.save(self.instance.image.file.name)
    #
    #     return result
