from ..models import train_classes, trip_seats, trips, bookings
from ..models.passengers import Passenger
from rest_framework.exceptions import NotFound
from django.core import serializers

from django.db.models import Count

def book_train_ticket(booking_details:dict):
    trip_id = booking_details.get("trip_id")
    passengers = booking_details.get("passengers")
    passenger_len = len(passengers)
    train_cabin_class = booking_details.get("train_cabin_class")
    # 1. check seats available in class or not 
    trip_seats_available = trip_seats.TripSeats.objects.filter(trip_id=trip_id, train_cabin_id__train_cabins__train_cabin_class_id=train_cabin_class, is_booked="N").order_by('seat_number')
    if trip_seats_available.count() < passenger_len:
        raise NotFound(f"No Seats available for {train_cabin_class} class, {trip_seats_available.count()} available")
    
    # 2. get cabins for that class, where seats can be allocated in one cabin or not
    get_available_cabins = trip_seats_available.values("train_cabin_id").order_by("train_cabin_id").annotate(count=Count("train_cabin_id")).filter(count__gte=passenger_len)
    if not get_available_cabins:
        raise NotFound(f"No Seats available in any of the cabins, to fit all the passengers")
    # create passenger and add the passenger
    available_train_cabin_id = get_available_cabins[0]['train_cabin_id']
    trip_seats_available_for_cabin = list(trip_seats_available.filter(train_cabin_id=available_train_cabin_id))
    # mark the booking
    trip = trips.Trip.objects.get(trip_id=trip_id)
    fare_price = train_classes.TrainCabinClass.objects.get(train_cabin_class_id=train_cabin_class).fair_price
    
    # import pdb;
    # pdb.set_trace()
    passengers_list = []
    for trip_seat, passenger in zip(trip_seats_available_for_cabin, passengers):
        trip_seat.is_booked = "Y"
        passenger['trip_seat']  = trip_seat
        passenger_obj = Passenger(**passenger)
        passenger_obj.save()
        passengers_list.append(passenger_obj)
        trip_seat.save()
    booking_obj = bookings.Booking(trip=trip, total_cost=(fare_price*passenger_len))
    booking_obj.passengers.set(passengers_list)
    booking_obj.save()
    return booking_obj