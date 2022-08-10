from django.db import models

# Create your models here.
class Student(models.Model):
    shoe = models.DecimalField(max_digits=5, decimal_places=1)
    board = models.CharField(max_length=100, blank=True)
    stance = models.CharField(max_length=200, blank=True)