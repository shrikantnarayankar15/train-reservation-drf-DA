from django.shortcuts import render
from django.db import transaction
from rest_framework.exceptions import APIException

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers.seriliazers import *
from .serializers.book_train_ticket_ser import BookTrainTicketSerializer
from .logic import register_trip_seats, book_train_ticket
from .models import (
    bookings,
    passengers,
    train_cabins,
    train_classes,
    trains,
    trip_seats,
    trips,
)


# class BookingPassengerViewSet(APIView):
#     def get(self, request, id):
#         obj = booking_passenger.BookingPassenger.objects.filter(booking_id=id)
#         ser = BookingPassengerSerializer(obj, many=True)
#         return Response({"data":ser.data}, status=200)


class BookingsViewSet(APIView):
    def get(self, request):
        obj = bookings.Booking.objects.all()
        ser = BookingSerializer(obj, many=True)
        return Response({"data": ser.data}, status=200)


class BookingViewSet(APIView):
    def get(self, request, id):
        obj = bookings.Booking.objects.get(booking_id=id)
        ser = BookingPassengerSerializer(obj)
        return Response({"data": ser.data}, status=200)


class PassengerViewSet(APIView):
    def get(self, request):
        obj = passengers.Passenger.objects.all()
        ser = PassengerSerializer(obj, many=True)
        return Response({"data": ser.data}, status=200)


# class TrainCabinPerTrainViewSet(APIView):
#     def get(self, request):
#         obj = train_cabin_per_train.TrainCabinPerTrain.objects.all()
#         ser = TrainCabinPerTrainSerializer(obj, many=True)
#         return Response({"data":ser.data}, status=200)


class TrainCabinViewSet(APIView):
    def get(self, request):
        obj = train_cabins.TrainCabin.objects.all()
        ser = TrainCabinSerializer(obj, many=True)
        return Response({"data": ser.data}, status=200)


class TrainCabinClassViewSet(APIView):
    def get(self, request):
        obj = train_classes.TrainCabinClass.objects.all()
        ser = TrainCabinClassSerializer(obj, many=True)
        return Response({"data": ser.data}, status=200)


class TrainViewSet(APIView):
    def get(self, request):
        obj = trains.Train.objects.all()
        ser = TrainSerializer(obj, many=True)
        return Response({"data": ser.data}, status=200)


class TripSeatsViewSet(APIView):
    def get(self, request):
        obj = trip_seats.TripSeats.objects.all()
        ser = TripSeatsSerializer(obj, many=True)
        return Response({"data": ser.data}, status=200)


class TripViewSet(APIView):
    def get(self, request, tripid=None):
        if tripid:
            obj = trips.Trip.objects.get(trip_id=tripid)
            ser = TripSerializer(obj)
            return Response({"data": ser.data}, status=200)
        obj = trips.Trip.objects.all()
        ser = TripSerializer(obj, many=True)
        return Response({"data": ser.data}, status=200)

    def delete(self, request, tripid, *args, **kwargs):
        trip_obj = trips.Trip.objects.get(trip_id=tripid)
        trip_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request):
        # 1. register trip seats for the train for that date
        response = {"status": "error", "status_code": status.HTTP_400_BAD_REQUEST}
        with transaction.atomic():
            trip_ser = TripSerializer(data=request.data)
            if trip_ser.is_valid():
                trip_ser.save()
                register_trip_seats.create_trip_seats_for_train(
                    trip_id=trip_ser.data["trip_id"], train_id=trip_ser.data["train_id"]
                )
                response["status"] = "success"
                response["data"] = trip_ser.data
                response["status_code"] = status.HTTP_200_OK

            else:
                response["data"] = trip_ser.errors
        return Response(response, status=response["status_code"])


class BookTrainTicket(APIView):
    def get(self, request, train_id=None, trip_id=None):
        if train_id:
            obj = trains.Train.objects.get(train_id=train_id)
            ser = TrainSerializer(obj)
            if trip_id:
                obj = trips.Trip.objects.get(trip_id=trip_id, train_id=train_id)
                ser = TripSerializer(obj)
                return Response({"data": ser.data}, status=200)
            obj = trips.Trip.objects.all()
            ser = TripSerializer(obj, many=True)
            return Response({"data": ser.data}, status=200)
        else:
            obj = trains.Train.objects.all()
            ser = TrainSerializer(obj, many=True)
            return Response({"data": ser.data}, status=200)

    def post(self, request, train_id, trip_id):
        # 1. selects the trip
        # 2. enters the passenger lists
        # 3. user selects the class
        # 4. checks seats present in the cabin
        # 5. if available, sequentially allocate the seats
        # get passenger details

        input_data = {"trip_id": trip_id}
        input_data.update(request.data)
        response = {"status": "error", "status_code": status.HTTP_400_BAD_REQUEST}
        with transaction.atomic():
            book_train_ticket_ser = BookTrainTicketSerializer(data=input_data)
            if book_train_ticket_ser.is_valid():
                # trip_ser.save()
                booking_obj = book_train_ticket.book_train_ticket(
                    booking_details=book_train_ticket_ser.data
                )
                response["status"] = "success"
                response["data"] = BookingSerializer(booking_obj).data
                response["status_code"] = status.HTTP_200_OK
            else:
                response["data"] = book_train_ticket_ser.errors
        # import json
        return Response(response, status=response["status_code"])
