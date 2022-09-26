from django.contrib.auth.models import AbstractUser
from django.db import models

from taxi_service import settings


class Manufacturer(models.Model):

    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]


class Car(models.Model):

    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL)

    class Meta:
        ordering = ["model"]


class Driver(AbstractUser):

    license_number = models.CharField(
        max_length=255, null=True, blank=True, unique=True
    )

    class Meta:
        ordering = ["username"]
