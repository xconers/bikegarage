# === Stage 3: Хранилище в памяти ===
# Project: BikeGarage
from datetime import date


class Bike:
    def __init__(self, bike_id, name, bike_type, mileage, service_date):
        self.id = bike_id
        self.name = name
        self.type = bike_type
        self.mileage = mileage
        self.service_date = service_date

    def __repr__(self):
        return (
            f"Bike(id={self.id}, name={self.name!r}, type={self.type!r}, "
            f"mileage={self.mileage}, service_date={self.service_date!r})"
        )


class BikeStorage:
    def __init__(self):
        self._bikes = {}

    def add_bike(self, bike):
        if bike.id in self._bikes:
            raise ValueError(f"Bike with id {bike.id} already exists")
        self._bikes[bike.id] = bike

    def get_bike(self, bike_id):
        return self._bikes.get(bike_id)

    def list_bikes(self):
        return list(self._bikes.values())

    def update_bike(self, bike):
        self._bikes[bike.id] = bike

    def remove_bike(self, bike_id):
        return self._bikes.pop(bike_id, None)


if __name__ == "__main__":
    storage = BikeStorage()

    first = Bike(1, "Racer X", "Mountain", 1500, date(2025, 1, 10))
    second = Bike(2, "City Cruiser", "Road", 800, date(2025, 2, 5))
    storage.add_bike(first)
    storage.add_bike(second)

    print("List of bikes:")
    for bike in storage.list_bikes():
        print(bike)

    print()
    print("Bike with id 1:")
    print(storage.get_bike(1))

    print()
    print("Bike with id 99 (not found):")
    print(storage.get_bike(99))

    try:
        storage.add_bike(Bike(1, "Duplicate", "Road", 0, date(2025, 3, 1)))
    except ValueError as error:
        print("Cannot add duplicate:", error)

    updated = Bike(2, "City Cruiser Updated", "Road", 850, date(2025, 2, 20))
    storage.update_bike(updated)
    print()
    print("Updated bike with id 2:")
    print(storage.get_bike(2))

    storage.remove_bike(1)
    print()
    print("Bikes after removing id 1:")
    for bike in storage.list_bikes():
        print(bike)
