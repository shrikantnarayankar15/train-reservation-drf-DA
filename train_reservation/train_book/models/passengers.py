
from django.db import models
from .trip_seats import TripSeats 
import uuid
# from .bookings import Booking
# Create your models here.
class Passenger(models.Model):
    passenger_id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    name = models.CharField(max_length=100)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    trip_seat = models.OneToOneField(TripSeats, on_delete=models.CASCADE, related_name="passenger")