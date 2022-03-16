from django.db import models
from django.contrib.auth.models import AbstractUser
from user.managers import CustomUserManager


class User(AbstractUser):
    """
    this class created for adding the table in database
    """

    username = models.CharField(max_length=40, unique=True, null=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.username
