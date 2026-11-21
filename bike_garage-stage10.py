# === Stage 10: Быстрые фильтры ===
# Project: BikeGarage
from datetime import datetime, timedelta


def parse_record(raw):
    parts = raw.split(";")
    name, bike_type, mileage, service_date = parts[0], parts[1], int(parts[2]), parts[3]
    return {
        "name": name,
        "type": bike_type,
        "mileage": mileage,
        "service_date": datetime.strptime(service_date, "%Y-%m-%d"),
    }


def format_record(record):
    return f"{record['name']} ({record['type']}, пробег: {record['mileage']}, " \
           f"обслуживание: {record['service_date'].strftime('%Y-%m-%d')})"


def today_filter(records, now=None):
    if now is None:
        now = datetime.now()
    today = now.date()
    return [r for r in records if r["service_date"].date() == today]


def this_week_filter(records, now=None):
    if now is None:
        now = datetime.now()
    start = now - timedelta(days=now.weekday())
    end = start + timedelta(days=6)
    return [r for r in records if start.date() <= r["service_date"].date() <= end.date()]


def overdue_filter(records, now=None):
    if now is None:
        now = datetime.now()
    return [r for r in records if r["service_date"].date() < now.date()]


def apply_filter(records, mode):
    if mode == "today":
        return today_filter(records)
    if mode == "week":
        return this_week_filter(records)
    if mode == "overdue":
        return overdue_filter(records)
    raise ValueError(f"Неизвестный фильтр: {mode}")


if __name__ == "__main__":
    demo = [
        parse_record("Горный-1;mountain;12000;2025-06-10"),
        parse_record("Грузовой-2;cargo;8500;2025-06-17"),
        parse_record("Гонщик-3;road;3400;2025-05-01"),
    ]
    for mode in ("today", "week", "overdue"):
        result = apply_filter(demo, mode)
        print(f"Фильтр '{mode}':")
        if result:
            for r in result:
                print("  " + format_record(r))
        else:
            print("  (пусто)")
