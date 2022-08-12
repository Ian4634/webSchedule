from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 50)
    shoe = models.CharField(max_length=10, blank=True)
    board = models.CharField(max_length=100, blank=True)
    stance = models.CharField(max_length=200, blank=True)
    bindingSize = models.CharField(max_length = 200, blank=True)