from django.contrib import admin
from .models import  bookings, passengers, train_cabins, train_classes,trains,trip_seats, trips
# Register your models here.

admin.site.register(bookings.Booking)
admin.site.register(passengers.Passenger)
admin.site.register(train_cabins.TrainCabin)
admin.site.register(train_classes.TrainCabinClass)
admin.site.register(trains.Train)
admin.site.register(trip_seats.TripSeats) 
admin.site.register(trips.Trip) 
