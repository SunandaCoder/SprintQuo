from django.db import models


class Sprint(models.Model):
    """
    This class is created for Sprint
    """
    sprint_name = models.CharField(max_length=200)
    start_date = models.CharField(max_length=20)
    end_date = models.CharField(max_length=20)


class Parameter(models.Model):
    """
    This class is created for parameter name
    """
    parameter_name = models.CharField(max_length=100)
