from pickle import FALSE
from django.db import models
from django.contrib.auth.models import AbstractUser
from tomlkit import boolean

# Create your models here.

class CustomUser(AbstractUser):
    subscribed = models.BooleanField(default=False)
