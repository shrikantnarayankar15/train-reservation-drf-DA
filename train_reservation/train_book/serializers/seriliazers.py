from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from ..models import (
    bookings,
    passengers,
    train_cabins,
    train_classes,
    trains,
    trip_seats,
    trips,
)


class BookingSerializer(ModelSerializer):
    class Meta:
        model = bookings.Booking
        fields = "__all__"


class BookingSerializer(ModelSerializer):
    class Meta:
        model = bookings.Booking
        fields = "__all__"


class PassengerSerializer(ModelSerializer):
    class Meta:
        model = passengers.Passenger
        fields = "__all__"


class BookingPassengerSerializer(ModelSerializer):
    passengers = PassengerSerializer(many=True)

    class Meta:
        model = bookings.Booking
        fields = "__all__"


class PassengerWithoutTripSeatSerializer(ModelSerializer):
    class Meta:
        model = passengers.Passenger
        exclude = ["trip_seat"]


class BookingTripSerializer(Serializer):
    booking_id = serializers.CharField(max_length=100)
    passenger_id = PassengerSerializer()


class TrainCabinSerializer(ModelSerializer):
    class Meta:
        model = train_cabins.TrainCabin
        fields = "__all__"


class TrainCabinClassSerializer(ModelSerializer):
    class Meta:
        model = train_classes.TrainCabinClass
        fields = "__all__"


class TrainSerializer(ModelSerializer):
    class Meta:
        model = trains.Train
        fields = "__all__"


class TripSeatsSerializer(ModelSerializer):
    class Meta:
        model = trip_seats.TripSeats
        fields = "__all__"


class TripSerializer(ModelSerializer):
    class Meta:
        model = trips.Trip
        fields = "__all__"
