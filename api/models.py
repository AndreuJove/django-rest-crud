import uuid

from django.db import models


# Create your models here.
class Aircraft(models.Model):
    serial_number = models.IntegerField(primary_key=True)
    manufacturer = models.CharField(max_length=255)


class Flight(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    departure_airport = models.CharField(max_length=200)
    departure_timestamp = models.DateTimeField()
    arrival_airport = models.CharField(max_length=200)
    arrival_timestamp = models.DateTimeField(
        null=True,
    )
    assigned_to = models.ForeignKey(
        Aircraft,
        related_name="flights",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
