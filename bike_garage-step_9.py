# === Stage 9: Группировка ===
# Project: BikeGarage
def group_bikes_by_type(bikes):
    groups = {}
    for bike in bikes:
        bike_type = bike["type"]
        if bike_type in groups:
            groups[bike_type] += 1
        else:
            groups[bike_type] = 1
    return groups


def count_bikes_by_type(bikes):
    groups = group_bikes_by_type(bikes)
    for bike_type, count in groups.items():
        print(f"Тип: {bike_type}, Количество: {count}")


if __name__ == "__main__":
    sample_bikes = [
        {"name": "Mountain Bike", "type": "mountain", "mileage": 500, "last_service": "2024-01-01"},
        {"name": "Road Bike", "type": "road", "mileage": 1000, "last_service": "2024-02-01"},
        {"name": "City Bike", "type": "city", "mileage": 300, "last_service": "2024-03-01"},
        {"name": "Mountain Bike 2", "type": "mountain", "mileage": 700, "last_service": "2024-04-01"},
        {"name": "Road Bike 2", "type": "road", "mileage": 1200, "last_service": "2024-05-01"},
    ]
    count_bikes_by_type(sample_bikes)
