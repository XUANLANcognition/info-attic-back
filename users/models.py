from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avatar = models.CharField(max_length=100, blank=True, default='')
    bio = models.CharField(max_length=150, blank=True, default='')

    class Meta(AbstractUser.Meta):
        pass

# Create your models here.
