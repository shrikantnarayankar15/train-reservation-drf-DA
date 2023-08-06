from rest_framework.serializers import Serializer
from rest_framework import serializers
from .seriliazers import PassengerWithoutTripSeatSerializer
from .seriliazers import TripSerializer

class BookTrainTicketSerializer(Serializer):
    trip_id = serializers.CharField(max_length=100)
    passengers = PassengerWithoutTripSeatSerializer(many=True)
    train_cabin_class = serializers.CharField(max_length=100)
