from django.db import models
from user.models import User


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


class Votes(models.Model):
    """
    This class is created for votes records
    """
    sprint_id = models.ForeignKey(Sprint, on_delete=models.CASCADE)
    parameter_id = models.ForeignKey(Parameter, on_delete=models.CASCADE)
    vote_by = models.ForeignKey(User, related_name='vote_by', on_delete=models.CASCADE)
    vote_for = models.ForeignKey(User, related_name='vote_for', on_delete=models.CASCADE)
