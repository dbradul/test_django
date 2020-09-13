# Generated by Django 3.1 on 2020-09-13 06:32

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    replaces = [('students', '0001_initial'), ('students', '0002_auto_20200830_1007'), ('students', '0003_group'), ('students', '0004_auto_20200906_0816'), ('students', '0005_student_email'), ('students', '0006_auto_20200909_1320'), ('students', '0007_auto_20200909_1333'), ('students', '0008_auto_20200909_1340'), ('students', '0009_auto_20200909_1354'), ('students', '0010_student_uuid'), ('students', '0011_student_phone'), ('students', '0012_auto_20200910_1754'), ('students', '0013_auto_20200910_1802'), ('students', '0014_auto_20200910_1803'), ('students', '0015_auto_20200913_0629'), ('students', '0016_auto_20200913_0630')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=84)),
                ('birthdate', models.DateTimeField(default=datetime.date.today, null=True)),
                ('rating', models.SmallIntegerField(default=0, null=True)),
                ('email', models.EmailField(max_length=128, null=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, null=True)),
            ],
        ),
    ]
