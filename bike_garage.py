# === Stage 1: Каркас модуля ===
# Project: BikeGarage
from dataclasses import dataclass, field
from datetime import date


@dataclass
class Bicycle:
    name: str
    type: str
    mileage: int
    service_date: date


def create_demo_bicycles() -> list:
    return [
        Bicycle(name="City Cruiser", type="city", mileage=1500, service_date=date(2024, 1, 15)),
        Bicycle(name="Mountain Pro", type="mountain", mileage=5200, service_date=date(2023, 11, 2)),
        Bicycle(name="Road Racer", type="road", mileage=890, service_date=date(2024, 3, 20)),
    ]


def main() -> None:
    bikes = create_demo_bicycles()
    print("BikeGarage: гараж велосипедов")
    print("В гараже находится {} велосипедов".format(len(bikes)))
    for bike in bikes:
        print("{} ({}, пробег: {} км, обслуживание: {})".format(
            bike.name, bike.type, bike.mileage, bike.service_date))


if __name__ == "__main__":
    main()
