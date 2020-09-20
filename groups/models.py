import datetime
import random

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
# from students.models import Student


class Classroom(models.Model):
    name = models.CharField(max_length=32)
    floor = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(2), MaxValueValidator(5)]
    )

    def __str__(self):
        return f'{self.name}, {self.floor}'


class Group(models.Model):
    name = models.CharField(max_length=64)
    course = models.CharField(max_length=128)
    start_date = models.DateField(null=True, default=datetime.date.today)
    head = models.OneToOneField(
        to='students.Student',
        null=True,
        on_delete=models.SET_NULL,
        related_name='head_of_group'
    )

    classrooms = models.ManyToManyField(
        to=Classroom,
        related_name='groups'
    )


    def __str__(self):
        return f'{self.name} ({self.course})'

    @staticmethod
    def generate_group():

        group = Group(
            name=f'Group - {random.choice(range(5))}',
            course=random.choice([
                "IT 210: Web Application Development.",
                "IT 226: Enterprise Information Systems.",
                "IT 227: E-Commerce Technologies.",
                "IT 238: Networking and Client/Server Computing.",
                "IT 280: Internet Security.",
                "IT 295: IT-Based Application Project.",
                "IT 299: Graduate Seminar.",
            ])
        )

        group.save()
