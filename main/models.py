from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager

# Create your models here.

class Day(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=10)

class Difficulty(models.Model):
    def __str__(self):
        return self.name
    difficulty = models.CharField(max_length=10)


class Activity(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    streetAddress = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=25,blank=True)
    state = models.CharField(max_length=25,blank=True)
    areaCode = models.CharField(max_length=5)
    country=models.CharField(max_length=25,blank=True)

    startDate = models.DateField()
    endDate = models.DateField()
    startTime = models.TimeField()
    endTime = models.TimeField()
    frequency = models.CharField(max_length=50)
    price = models.CharField(max_length=10, blank=True)
    thumbnail = models.ImageField(blank=True, upload_to='images/')
    activityPage= models.URLField(blank=True)
    hostName = models.CharField(max_length=25, blank=True)
    participants =models.IntegerField(blank=True,default=5)

    minAge = models.IntegerField(blank=True, default=5)
    maxAge = models.IntegerField(blank=True, default=10)

    BEGINNER = 'Beginner'
    INTERMEDIATE = 'Intermediate'
    ADVANCED = 'Advanced'
    DIFFICULTY_LEVEL = [
        (BEGINNER, 'Beginner'),
        (INTERMEDIATE, 'Intermediate'),
        (ADVANCED, 'Advanced'),
    ]
    difficulty = models.CharField(max_length=25,choices=DIFFICULTY_LEVEL, blank=True)

    tags = TaggableManager()
    days_of_week = models.ManyToManyField(Day)

