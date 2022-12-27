from django.db import models
from django.utils import timezone

# Create your models here.

class Activity(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    areaCode = models.CharField(max_length=5)
    startDate = models.DateField()
    endDate = models.DateField()
    startTime = models.TimeField()
    endTime = models.TimeField()
    frequency = models.CharField(max_length=50)

