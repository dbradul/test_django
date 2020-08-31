import datetime

from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=84, null=False)
    birthdate = models.DateTimeField(null=True, default=datetime.date.today)


class Group(models.Model):
    group_number = models.IntegerField()
    # curator = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, related_name='student_id')
    starting_date = models.DateTimeField()