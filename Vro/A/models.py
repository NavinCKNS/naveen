from django.db import models

class temp(models.Model):
    name=models.CharField(max_length=10)
    cls=models.IntegerField()
    section=models.CharField(max_length=2)

