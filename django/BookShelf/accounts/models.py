from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom user model extending Django's AbstractUser
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.username