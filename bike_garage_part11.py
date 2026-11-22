# === Stage 11: Поиск дубликатов ===
# Project: BikeGarage
def normalize_bike(bike):
    if isinstance(bike, dict):
        title = bike.get("название", "")
        type_ = bike.get("тип", "")
        mileage = bike.get("пробег", 0)
        service = bike.get("дата обслуживания", "")
    else:
        title = getattr(bike, "название", "")
        type_ = getattr(bike, "тип", "")
        mileage = getattr(bike, "пробег", 0)
        service = getattr(bike, "дата обслуживания", "")

    title = str(title).strip().lower()
    type_ = str(type_).strip().lower()
    try:
        mileage = float(mileage)
    except (TypeError, ValueError):
        mileage = 0.0
    service = str(service).strip().lower()

    return f"{title}|{type_}|{mileage}|{service}"


def find_duplicate_bikes(bikes):
    seen = {}
    duplicates = []

    for bike in bikes:
        key = normalize_bike(bike)
        if key in seen:
            duplicates.append(bike)
        else:
            seen[key] = bike

    return duplicates
