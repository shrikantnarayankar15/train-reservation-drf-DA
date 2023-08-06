from django.db import models
from .trips import Trip
from .trains import Train
from .train_cabins import TrainCabin
# from .passengers import Passenger
import uuid
# Create your models here.
class TripSeats(models.Model):
    trip_id = models.ForeignKey(Trip, on_delete=models.CASCADE)
    train_id = models.ForeignKey(Train, on_delete=models.CASCADE)
    train_cabin_id = models.ForeignKey(TrainCabin, on_delete=models.CASCADE)
    seat_number = models.IntegerField()
    BOOKING_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    is_booked = models.CharField(max_length=1, choices=BOOKING_CHOICES)