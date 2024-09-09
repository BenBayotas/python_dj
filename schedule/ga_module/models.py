from django.db import models

# Create your models here.

class Subject(models.Model):
    subject_code = models.CharField(max_length=255)
    subject_name = models.CharField(max_length=255)
    subject_time = models.CharField(max_length=255, null=True)
    subject_day = models.CharField(max_length=255, null=True)

class Teacher(models.Model):
    teacher_id = models.IntegerField()
    teacher_name = models.CharField(max_length=255)
    subject_code1 = models.CharField(max_length=255)
    subject_code2 = models.CharField(max_length=255)
    subject_code3 = models.CharField(max_length=255)

class Room(models.Model):
    LOCALE = {
        "CB" : "Main",
        "CBS": "South",
        "CBE": "East",
    }
    ROOM_TYPE = {
        "LEC": "Lecture",
        "LAB": "Laboratory",
    }

    room_id = models.CharField(max_length=255)
    room_locale = models.CharField(max_length=64, choices=LOCALE, default='CB')
    room_type = models.CharField(max_length=64, choices=ROOM_TYPE, default='LEC')