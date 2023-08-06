## This is a complete backend DRF (Django Rest Framework) based Application
- In database,
    - trains are already created
    - for each train there is train cabin (SC1, SC2, FC1, FC2) based on the cabin class
    - train cabin belongs to any of the class (FC, SC)
* Run `python3 manage.py runserver`
Below are the endpoints
```
1. admin/ -> admin api
2. trains/ -> to get all trains
3. trips/ -> get trips for each train
4. trips/<str:tripid> -> get trip details and create trip
5. bookings/ -> get all bookings
6. bookings/<str:id> -> get bookings for a booking id
7. passengers/ -> get all the passengers
8. traincabinclasses/ -> get all the train cabin classes
9. tripseats/ -> get tripseats
10. traincabins/ -> get train cabins 
11. book/trains -> get trains to book
12. book/trains/<str:train_id> -> get train details
13. book/trains/<str:train_id>/trips/<str:trip_id> -> boook a trip for a train
```
## access-database 
- username: admin
- password: shrikant
1. First we create trip for a date
- open `http://localhost:8000/trips/`
- insert following into "Content"
```
{
    "date": "2023-08-01", (date you can change)
    "train_id": "db1d890b-575e-4774-973a-ffb12f19383c" (train id)
}
```

- click on POST
- Trip Seats will be created based on the train for each cabin
- to get all the seats for a trip, go to `http://localhost:8000/tripseats/`
3. Book a ticket
- go to below link
- http://localhost:8000/book/trains/{train_id}/trips/{trip_id}
- in our case it will be
- open `http://localhost:8000/book/trains/db1d890b-575e-4774-973a-ffb12f19383c/trips/a4d427fc-2bab-434a-a567-efbe17b9c6e1`
- insert following into "Content"
```
    {
        "train_cabin_class": "FC", 
        "passengers": [
            {
                "name": "pass1",
                "gender": "M"
            },
            {
                "name": "pass2",
                "gender": "M"
            }
        ]
    }
```
-- train_cabin_class-> for which class, you want to book the passengers
-- passengers -> list of passengers
- click on POST
- booking will be created
```
{
    "status": "success",
    "status_code": 200,
    "data": {
        "booking_id": "38367df7-077c-4be4-9c62-43b10d9277aa",
        "total_cost": 200,
        "trip": "a4d427fc-2bab-434a-a567-efbe17b9c6e1",
        "passengers": [
            "4c82e387-601d-4251-bab6-a317aa44b2bc",
            "b1341f00-0e80-4952-b316-7f8c712d4d9d"
        ]
    }
}
```
- to check details for the booking go to below site
- `http://localhost:8000/bookings/{booking_id}`
- `http://localhost:8000/bookings/38367df7-077c-4be4-9c62-43b10d9277aa`
- output
```
{
    "data": {
        "booking_id": "38367df7-077c-4be4-9c62-43b10d9277aa", # booking id
        "passengers": [ # passengers
            {
                "passenger_id": "4c82e387-601d-4251-bab6-a317aa44b2bc",
                "name": "shri",
                "gender": "M",
                "trip_seat": 1
            },
            {
                "passenger_id": "b1341f00-0e80-4952-b316-7f8c712d4d9d",
                "name": "shri",
                "gender": "M",
                "trip_seat": 2
            }
        ],
        "total_cost": 200, # total cost of the booking
        "trip": "a4d427fc-2bab-434a-a567-efbe17b9c6e1" # for which trip
    }
}
```

1. If there are no seats available for the cabin class then error is thrown
`No Seats available for {train_cabin_class} class, {trip_seats_available.count()} available`
2. If there are no seats available for the cabin then error is thrown
`No Seats available in any of the cabins, to fit all the passengers`