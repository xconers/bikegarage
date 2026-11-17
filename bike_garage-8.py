# === Stage 8: Теги ===
# Project: BikeGarage
class BikeTagError(ValueError):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class BikeTag:
    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise BikeTagError("Тег должен быть непустой строкой")
        self.name = name.strip()


class BikeTags:
    def __init__(self):
        self._tags = {}

    def add(self, bike, tag):
        if not isinstance(tag, BikeTag):
            raise BikeTagError("Метка должна быть объектом BikeTag")
        tag_name = tag.name
        tags = self._tags.get(bike.name, [])
        if tag_name not in tags:
            tags.append(tag_name)
        self._tags[bike.name] = tags
        return tag

    def remove(self, bike, tag):
        if not isinstance(tag, BikeTag):
            raise BikeTagError("Метка должна быть объектом BikeTag")
        tag_name = tag.name
        tags = self._tags.get(bike.name, [])
        if tag_name in tags:
            tags.remove(tag_name)
            self._tags[bike.name] = tags
            return True
        return False

    def find(self, bike, tag):
        if not isinstance(tag, BikeTag):
            raise BikeTagError("Метка должна быть объектом BikeTag")
        tag_name = tag.name
        return tag_name in self._tags.get(bike.name, [])


class BikeTagRepository:
    def __init__(self):
        self._bikes = {}
        self._tags = {}

    def add_bike(self, bike):
        self._bikes[bike.name] = bike

    def add_tag(self, bike, tag):
        if bike.name not in self._bikes:
            raise BikeTagError("Велосипед не найден в гараже")
        bike_tags = self._tags.setdefault(bike.name, [])
        if tag.name not in bike_tags:
            bike_tags.append(tag.name)
        return tag

    def remove_tag(self, bike, tag):
        if bike.name not in self._bikes:
            raise BikeTagError("Велосипед не найден в гараже")
        bike_tags = self._tags.get(bike.name, [])
        if tag.name in bike_tags:
            bike_tags.remove(tag.name)
            return True
        return False

    def find_by_tag(self, tag):
        if not isinstance(tag, BikeTag):
            raise BikeTagError("Метка должна быть объектом BikeTag")
        tag_name = tag.name
        result = []
        for bike_name, bike_tags in self._tags.items():
            if tag_name in bike_tags:
                result.append(self._bikes[bike_name])
        return result
