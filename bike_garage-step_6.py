# === Stage 6: Генерация идентификаторов ===
# Project: BikeGarage
PREFIX = "bike"


class IDCollisionError(Exception):
    def __init__(self, identifier, prefix):
        self.identifier = identifier
        self.prefix = prefix
        super().__init__(f"Уникальный идентификатор {prefix}:{identifier} уже существует")


def is_reserved(name):
    if name is None:
        return True
    return not (isinstance(name, str) and name.strip())


def generate_unique_id(name, prefix=PREFIX):
    if is_reserved(name):
        raise ValueError("Идентификатор не может быть пустым или None")

    base = "".join(ch for ch in str(name).strip().lower() if ch.isalnum() or ch == "_")
    candidate = f"{prefix}:{base}"

    while candidate in RESERVED_NAMES:
        candidate = f"{prefix}:{base}{len(RESERVED_NAMES)}"

    RESERVED_NAMES.add(candidate)
    return candidate


RESERVED_NAMES = set()


def clear_reserved_names():
    RESERVED_NAMES.clear()


def get_reserved_names():
    return set(RESERVED_NAMES)


if __name__ == "__main__":
    first = generate_unique_id("Shimano")
    print("Первый:", first)

    second = generate_unique_id("Shimano")
    print("Второй:", second)

    third = generate_unique_id("Road Bike")
    print("Третий:", third)

    try:
        generate_unique_id("   ")
    except ValueError as error:
        print("Ошибка:", error)
