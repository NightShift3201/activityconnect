from django.db import models

# Create your models here.

class Activity(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    areaCode = models.CharField(max_length=5)
    
