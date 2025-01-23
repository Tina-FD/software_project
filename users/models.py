from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLES = (
        ('admin', 'Admin'),
        ('editor', 'Editor'),
        ('user', 'User'),
    )
    
    phone = models.CharField(max_length=15)
    role = models.CharField(max_length=10, choices=ROLES, default='user')