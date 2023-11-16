from django.db import models
from django.urls import reverse
class student(models.Model):
    name=models.CharField(max_length=20)
    fathername=models.CharField(max_length=20)
    classname=models.IntegerField()
    contact=models.CharField(max_length=10)
class teachers(models.Model):
    name=models.CharField(max_length=20)
    subject=models.CharField(max_length=20)
    exp=models.IntegerField()
    contact=models.CharField(max_length=10)
    def get_absolute_url(self):
        return reverse("list")