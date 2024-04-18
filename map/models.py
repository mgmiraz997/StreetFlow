from django.db import models


class Vehicle(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
