# Generated by Django 3.1 on 2020-09-20 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_auto_20200916_1819'),
        ('groups', '0003_remove_group_head'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='head',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='head_of_group', to='students.student'),
        ),
    ]