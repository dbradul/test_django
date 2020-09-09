from django import forms
from django.core.exceptions import ValidationError

from students.models import Student


class StudentCreateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'rating', 'email']

    def clean_email(self):
        email = self.cleaned_data['email']

        blacklist_domains = [
            'mail.ru',
            'yandex.ru'
        ]

        domain = email.split('@')[1]

        if domain in blacklist_domains:
            raise ValidationError('Prohibited domain')

        return email