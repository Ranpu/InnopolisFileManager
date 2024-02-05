import math


def calculate_taxi_fare(km, min_price=100, price_per_km=12):
    if km <= 3:
        total_fare = min_price
    else:
        total_fare = min_price + price_per_km * (math.ceil(km) - 3)
        # total_fare = min_price + price_per_km * (km - 3)

    return total_fare


if __name__ == "__main__":
    distance = 20.5
    print(
        f"Стоимость поездки за {distance} км: {calculate_taxi_fare(km=distance)} руб."
    )
