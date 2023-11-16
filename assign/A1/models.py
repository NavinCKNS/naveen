from django.db import models
from django.urls import reverse
class states(models.Model):
    name=models.CharField(max_length=20)
    capital=models.CharField(max_length=10)
    language=models.CharField(max_length=20)
    population=models.IntegerField()
