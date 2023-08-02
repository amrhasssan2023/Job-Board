from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Info(models.Model):
    place = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)

    def __str__(self):
        return self.email