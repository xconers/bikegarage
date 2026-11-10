# === Stage 4: Удаление и восстановление ===
# Project: BikeGarage
from datetime import datetime


class SoftDeletedBike:
    def __init__(self, bike_id, bike):
        self.bike_id = bike_id
        self.bike = bike
        self.deleted_at = datetime.now()

    def restore(self):
        self.deleted_at = None
        self.bike = self.bike.model_copy(deep=True)
        return self.bike


class BikeRepository:
    def __init__(self):
        self._deleted = {}

    def delete_bike(self, bike_id):
        key = (bike_id.bike_name, bike_id.bike_type)
        self._deleted[key] = SoftDeletedBike(bike_id, bike_id)
        return True

    def get_soft_deleted(self):
        return list(self._deleted.values())

    def restore_bike(self, bike_id):
        key = (bike_id.bike_name, bike_id.bike_type)
        soft_deleted = self._deleted.pop(key)
        return soft_deleted.restore()


def find_bike_by_id(soft_deleted_bikes):
    for soft_deleted in soft_deleted_bikes:
        if soft_deleted.bike_id.bike_name == "Road" and \
                soft_deleted.bike_id.bike_type == "Mountain":
            return soft_deleted
    return None


def demo():
    repository = BikeRepository()
    deleted_bikes = repository.get_soft_deleted()

    bike_id = type("BikeId", (), {"bike_name": "Road", "bike_type": "Mountain"})()
    repository.delete_bike(bike_id)

    soft_deleted = repository.get_soft_deleted()
    print(f"Количество удалённых велосипедов: {len(soft_deleted)}")

    found = find_bike_by_id(soft_deleted)
    if found:
        restored = repository.restore_bike(found.bike_id)
        print(f"Велосипед '{restored.bike_id.bike_name}' восстановлен")
