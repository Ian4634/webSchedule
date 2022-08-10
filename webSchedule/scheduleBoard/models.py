from django.db import models

# Create your models here.
class Lesson(models.Model):
    time = models.CharField(max_length=200)
    notes = models.CharField(max_length = 500)
    instructors = models.CharField(max_length = 200)
    student_names = models.CharField(max_length = 500, default='no info')