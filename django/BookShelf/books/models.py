from django.db import models
from django.conf import settings
# Create your models here.
class Books(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    cover=models.ImageField(uploaded_to ='covers/',blank=True)
    description=models.TextFiled(blank=True)
    added_by=models.ForeginKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='books'
    )