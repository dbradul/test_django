import datetime
import random

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.timezone import now

from faker import Faker

import uuid


# Create your models here.
from groups.models import Group
from students.validators import DomainValidator


class BaseModel(models.Model):
    class Meta:
        abstract = True

    create_date = models.DateTimeField(null=True, default=now)
    write_date = models.DateTimeField(null=True, default=now)

    def save(self, *args, **kwargs):
        self.write_date = datetime.datetime.now()
        super().save(*args, **kwargs)


class Person(BaseModel):
    class Meta:
        abstract = True

    first_name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=84, null=False)
    birthdate = models.DateTimeField(null=True, default=datetime.date.today)
    email = models.EmailField(null=True, max_length=128, validators=[DomainValidator()])
    uuid = models.UUIDField(null=True, max_length=64, default=uuid.uuid4)

    def full_name(self):
        return f'{self.first_name}, {self.last_name}'

    def age(self):
        return datetime.datetime.now().date().year - self.birthdate.year

    def __str__(self):
        return f'{self.id}, {self.full_name()}, {self.age()}'


class Student(Person):
    # first_name = models.CharField(max_length=64, null=False)
    # last_name = models.CharField(max_length=84, null=False)
    # birthdate = models.DateTimeField(null=True, default=datetime.date.today)
    # email = models.EmailField(null=True, max_length=128)
    # uuid = models.UUIDField(null=True, max_length=64, default=uuid.uuid4)

    rating = models.SmallIntegerField(null=True, default=0)
    group = models.ForeignKey(
        to=Group,
        null=True,
        on_delete=models.SET_NULL,
        related_name='students',
    )

    def __str__(self):
        return f'{super().__str__()}, {self.rating}'


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


class Teacher(Person):
    # first_name = models.CharField(max_length=64, null=False)
    # last_name = models.CharField(max_length=84, null=False)
    # birthdate = models.DateTimeField(null=True, default=datetime.date.today)
    # email = models.EmailField(null=True, max_length=128)
    # uuid = models.UUIDField(null=True, max_length=64, default=uuid.uuid4)
    specialization = models.EmailField(null=True, max_length=128)


    def __str__(self):
        return f'{super().__str__()}, {self.specialization}'
    #