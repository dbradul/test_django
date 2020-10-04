# Generated by Django 3.1 on 2020-09-27 11:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_auto_20200927_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='write_date',
            field=models.DateTimeField(default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='write_date',
            field=models.DateTimeField(default=datetime.datetime.now, null=True),
        ),
    ]