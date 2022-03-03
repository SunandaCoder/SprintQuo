from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    this class created for adding the table in database
    """

    mobile = models.IntegerField(verbose_name="MobileNo")
