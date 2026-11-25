# === Stage 12: Массовое обновление ===
# Project: BikeGarage
from datetime import datetime


def format_mileage(mileage):
    if mileage is None:
        return "-"
    return f"{mileage:.1f} км"


def format_date(value):
    if value is None:
        return "-"
    return value.strftime("%Y-%m-%d")


def preview_update(bikes, filter_fn, set_mileage, set_service_date):
    matched = [bike for bike in bikes if filter_fn(bike)]
    if not matched:
        print("Соответствующих велосипедов не найдено.")
        return

    print(f"Найдено велосипедов для обновления: {len(matched)}")
    print("\nПредварительный просмотр изменений:")
    print("=" * 70)

    for bike in matched:
        old_mileage = bike["mileage"]
        old_service = bike["service_date"]
        bike["mileage"] = set_mileage
        bike["service_date"] = set_service_date
        print(f"Велосипед: {bike['name']} ({bike['type']})")
        print(f"  Пробег:      {format_mileage(old_mileage)} -> {format_mileage(bike['mileage'])}")
        print(f"  Обслуживание: {format_date(old_service)} -> {format_date(bike['service_date'])}")
        print("-" * 70)


def main():
    bikes = [
        {"name": "Trek", "type": "Горный", "mileage": 1200.5, "service_date": datetime(2023, 5, 10)},
        {"name": "Cannondale", "type": "Шоссейный", "mileage": 3400.0, "service_date": datetime(2024, 1, 15)},
        {"name": "Specialized", "type": "Гибрид", "mileage": 800.0, "service_date": datetime(2024, 3, 20)},
    ]

    def is_high_mileage(bike):
        return bike["mileage"] >= 3000

    def new_mileage(bike):
        return bike["mileage"] * 2

    def new_service_date():
        return datetime.now()

    preview_update(bikes, is_high_mileage, new_mileage, new_service_date)


if __name__ == "__main__":
    main()
