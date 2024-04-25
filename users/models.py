from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    CHOICES = [
        ('1', 'Фрилансер'),
        ('2', 'Клиент'),
    ]
    role = models.CharField(max_length=20, choices=CHOICES, default='1')
    data = models.TextField()
