from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Logger(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    path = models.CharField(max_length=128)
    create_date = models.DateTimeField(auto_now_add=True)
    execution_time = models.FloatField()
    query_params = models.CharField(max_length=64, null=True)
    info = models.CharField(max_length=128, null=True)