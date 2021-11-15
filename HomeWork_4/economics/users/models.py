from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    location = models.CharField('Город проживания', max_length=32, null=True, blank=True)
    money = models.FloatField('Денежные средства', null=True, blank=True)
