"""
URL configuration for train_reservation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from train_book.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('trains/', TrainViewSet.as_view()),
    path('trips/', TripViewSet.as_view()),
    path('trips/<str:tripid>', TripViewSet.as_view()),
    path('bookings/', BookingsViewSet.as_view()),
    path('bookings/<str:id>', BookingViewSet.as_view()),
    path('passengers/', PassengerViewSet.as_view()),
    path('traincabinclasses/', TrainCabinClassViewSet.as_view()),
    # path('traincabinpertrain/', TrainCabinPerTrainViewSet.as_view()),
    # path('bookings/', BookingPassengerViewSet.as_view()),
    path('tripseats/', TripSeatsViewSet.as_view()),
    path('traincabins/', TrainCabinViewSet.as_view()),
    path('book/trains', BookTrainTicket.as_view()),
    path('book/trains/<str:train_id>', BookTrainTicket.as_view()),
    path('book/trains/<str:train_id>/trips/<str:trip_id>', BookTrainTicket.as_view()),
]
