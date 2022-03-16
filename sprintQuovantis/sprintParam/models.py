from datetime import datetime

from django.db import models


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
