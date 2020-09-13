import datetime
import random

from django.core.validators import MinLengthValidator, MaxLengthValidator, MaxValueValidator, MinValueValidator
from django.db import models

from faker import Faker

from uuid import uuid4


# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=84, null=False)
    birthdate = models.DateTimeField(null=True, default=datetime.date.today)
    rating = models.SmallIntegerField(null=True, default=0)
    email = models.EmailField(null=True, max_length=128)
    uuid = models.UUIDField(null=True, max_length=64, default=uuid4().hex)

    def full_name(self):
        return f'{self.first_name}, {self.last_name}'

    def age(self):
        return datetime.datetime.now().date().year - self.birthdate.year

    def __str__(self):
        return f'{self.id}, {self.full_name()}, {self.age()}, {self.rating}'

    @staticmethod
    def generate_students(count):

        faker = Faker()

        for _ in range(count):
            st = Student.objects.screate(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                rating=random.randint(0, 100)
            )
            st.save()
