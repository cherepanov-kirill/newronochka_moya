import random

number_of_flights = 150  # Максимальное кол-во полетов у пассажира
number_of_passenger = 2000  # Общее кол-во пассажирова в датасете


def create_passenger(number_of_flights):
    total_flights = random.randint(2, number_of_flights)
    cancelled_flights = random.randint(0, total_flights // 10)
    season = random.randint(0, 3)
    temp = [0 for i in range(total_flights - cancelled_flights)] + [
        1 for i in range(cancelled_flights)
    ]
    random.shuffle(temp)
    is_cancel = random.choice(temp)
    time_since_booking = random.randint(1, 365)
    passenger = {
        "total_flights": total_flights,
        "cancelled_flights": cancelled_flights,
        "time_since_booking": time_since_booking,
        "season_cancelled": season,
        "cancel_label": is_cancel,
    }
    return passenger


passengers = [create_passenger(number_of_flights) for i in range(number_of_passenger)]

with open("dataset.txt", "w+") as f:
    f.write(
        "total_flights,cancelled_flights,time_since_booking,season_cancelled,cancel_label\n"
    )
    for passenger in passengers:
        data = (f'{passenger["total_flights"]},{passenger["cancelled_flights"]},'
                f'{passenger["time_since_booking"]},{passenger["season_cancelled"]},'
                f'{passenger["cancel_label"]}\n')

        f.write(data)
