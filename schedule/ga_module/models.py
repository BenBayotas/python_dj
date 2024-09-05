from django.db import models

# Create your models here.

class Subject(models.Model):
    subject_code = models.CharField(max_length=255)
    subject_name = models.CharField(max_length=255)
    subject_time = models.CharField(max_length=255, null=True)
    subject_day = models.CharField(max_length=255, null=True)
