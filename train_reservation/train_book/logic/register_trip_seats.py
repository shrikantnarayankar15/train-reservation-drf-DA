from ..models import trip_seats, trips, trains

def create_trip_seats_for_cabin_for_train(trip, train, train_cabin):
    # [train_cabin.train_cabin_limit]
    # 1. get_train_cabin and its limit
    # 2. insert all the rows in the trip seats table for this cabin for this train

    trip_seats_for_cabin = [
        trip_seats.TripSeats(
            trip_id=trip,
            train_id=train,
            train_cabin_id=train_cabin,
            seat_number=i,
            # passenger_id=None,
            is_booked = "N"
        )
        for i in range(train_cabin.train_cabin_limit)
    ]
    trip_seats.TripSeats.objects.bulk_create(trip_seats_for_cabin)

def create_trip_seats_for_train(trip_id: str, train_id: str):
    # 1. get all the cabins for the train
    # 2. insert rows for each cabins in trip seats
    trip = trips.Trip(trip_id=trip_id)
    train = trains.Train(train_id=train_id)
    train_cabins = train.train_cabins.all()
    for train_cabin in train_cabins:
        create_trip_seats_for_cabin_for_train(
            trip=trip, train=train, train_cabin=train_cabin
        )
