from django.db import models
from .trips import Trip
from .train_classes import TrainCabinClass
from .passengers import Passenger
import uuid

class Booking(models.Model):
    booking_id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    total_cost = models.IntegerField()
    passengers = models.ManyToManyField(Passenger, null=True, related_name="booking")
