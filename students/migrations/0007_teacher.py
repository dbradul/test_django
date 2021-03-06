# Generated by Django 3.1 on 2020-09-27 10:10

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_auto_20200916_1819'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=84)),
                ('birthdate', models.DateTimeField(default=datetime.date.today, null=True)),
                ('email', models.EmailField(max_length=128, null=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, null=True)),
                ('specialization', models.EmailField(max_length=128, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
