# === Stage 7: Фильтрация записей ===
# Project: BikeGarage
def filter_bikes(bikes, bike_type=None, date_range=None):
    filtered = []
    for bike in bikes:
        if bike_type is not None and bike['type'] != bike_type:
            continue
        if date_range is not None:
            start, end = date_range
            if bike['service_date'] < start or bike['service_date'] > end:
                continue
        filtered.append(bike)
    return filtered


if __name__ == '__main__':
    sample_bikes = [
        {'name': 'Canyon', 'type': 'mountain', 'mileage': 1200, 'service_date': '2024-01-15'},
        {'name': 'Trek', 'type': 'road', 'mileage': 800, 'service_date': '2024-03-20'},
        {'name': 'Giant', 'type': 'mountain', 'mileage': 2000, 'service_date': '2023-11-10'},
        {'name': 'Specialized', 'type': 'road', 'mileage': 500, 'service_date': '2024-06-05'},
        {'name': 'Cannondale', 'type': 'hybrid', 'mileage': 900, 'service_date': '2024-02-28'},
    ]

    print("Всего велосипедов:", len(sample_bikes))
    print("Мountain bikes:", filter_bikes(sample_bikes, bike_type='mountain'))
    print("Road bikes:", filter_bikes(sample_bikes, bike_type='road'))
    print("Обслуживание в 2024:", filter_bikes(sample_bikes, date_range=('2024-01-01', '2024-12-31')))
    print("Mountain и 2024:", filter_bikes(sample_bikes, bike_type='mountain', date_range=('2024-01-01', '2024-12-31')))
