from django import forms
from django.core.exceptions import ValidationError

from students.models import Student


class StudentBaseForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'rating', 'email', 'group']

    def clean(self):
        pass

    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #
    #     blacklist_domains = [
    #         'mail.ru',
    #         'yandex.ru'
    #     ]
    #
    #     domain = email.split('@')[1]
    #
    #     if domain in blacklist_domains:
    #         raise ValidationError('Prohibited domain')
    #
    #     return email


class StudentCreateForm(StudentBaseForm):
    class Meta(StudentBaseForm.Meta):
        fields = ['first_name', 'last_name', 'rating', 'email', 'group']


class StudentEditForm(StudentBaseForm):
    class Meta(StudentBaseForm.Meta):
        fields = ['first_name', 'last_name', 'rating', 'email']
