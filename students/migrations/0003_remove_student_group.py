# Generated by Django 3.1 on 2020-09-16 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_student_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='group',
        ),
    ]
