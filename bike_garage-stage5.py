# === Stage 5: Связи между сущностями ===
# Project: BikeGarage
bike_garage_service.py

from datetime import datetime


class Bike:
    def __init__(self, name, bike_type, mileage):
        self.name = name
        self.bike_type = bike_type
        self.mileage = mileage
        self.service_records = []


class Service:
    def __init__(self, service_id, bike, service_date, description):
        self.service_id = service_id
        self.bike = bike
        self.service_date = service_date
        self.description = description


class Garage:
    def __init__(self):
        self.bikes = {}
        self.services = []
        self._service_counter = 0

    def add_bike(self, bike):
        self.bikes[bike.name] = bike

    def add_service(self, bike, service_date, description):
        self._service_counter += 1
        service = Service(self._service_counter, bike, service_date, description)
        self.services.append(service)
        if bike in self.bikes:
            bike.service_records.append(service)
        return service


def get_all_services_for_bike(garage, bike_name):
    target = garage.bikes.get(bike_name)
    if target is None:
        return None
    result = [s for s in garage.services if s.bike is target]
    return result


def verify_service_integrity(garage):
    errors = []
    for service in garage.services:
        if service.bike not in garage.bikes:
            errors.append(
                "service %s references unknown bike %s" % (
                    service.service_id, service.bike.name))
    for bike in garage.bikes.values():
        for service in bike.service_records:
            if not any(s is service for s in garage.services):
                errors.append(
                    "service %s in bike %s is not registered globally" % (
                        service.service_id, bike.name))
    return errors


def main():
    garage = Garage()
    garage.add_bike(Bike("Torque", "mountain", 1500))
    garage.add_bike(Bike("Comet", "road", 800))
    garage.add_service(garage.bikes["Torque"],
                      datetime(2024, 1, 15), "chain lube")
    garage.add_service(garage.bikes["Torque"],
                      datetime(2024, 3, 20), "brake check")
    garage.add_service(garage.bikes["Comet"],
                      datetime(2024, 2, 10), "tire replacement")

    torques = get_all_services_for_bike(garage, "Torque")
    for service in torques:
        print("Service %s on %s: %s" % (
            service.service_id, service.bike.name, service.description))

    errors = verify_service_integrity(garage)
    if errors:
        for error in errors:
            print("Integrity error:", error)
    else:
        print("All integrity checks passed.")


if __name__ == "__main__":
    main
