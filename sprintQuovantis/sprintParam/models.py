from datetime import datetime

from django.db import models
from user.models import User


class Sprint(models.Model):
    """
    This class is created for Sprint
    """
    sprint_name = models.CharField(max_length=200, unique=True, null=False)
    entry_date = models.DateTimeField(default=datetime.now)
    expiry_date = models.DateField()

    @property
    def is_expired(self):
        if datetime.now > self.expiry_date:
            return True
        return False


class Parameter(models.Model):
    """
    This class is created for parameter name
    """
    parameter_name = models.CharField(max_length=100, unique=True, null=False)


class Votes(models.Model):
    """
    This class is created for votes records
    """
    sprint_id = models.ForeignKey(Sprint, on_delete=models.CASCADE)
    parameter_id = models.ForeignKey(Parameter, on_delete=models.CASCADE)
    vote_by = models.ForeignKey(User, related_name='vote_by', on_delete=models.CASCADE)
    vote_for = models.ForeignKey(User, related_name='vote_for', on_delete=models.CASCADE)
