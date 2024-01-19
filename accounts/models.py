from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    mobile = models.CharField(max_length=12, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
