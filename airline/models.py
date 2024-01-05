from django.db import models

# Create your models here.
class flight(models.Model):
    source=models.CharField(max_length=40)
    destination=models.CharField(max_length=40)
    duration=models.CharField(max_length=20)

