# Generated by Django 3.1 on 2020-09-16 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_group_head'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='head',
        ),
    ]
