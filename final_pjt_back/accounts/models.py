from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True) 
    age = models.IntegerField(blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    asset = models.IntegerField(blank=True, null=True)
    target_asset = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    # Text
    financial_products = models.TextField(blank=True, null=True)
    # superuser fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'