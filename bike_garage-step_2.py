# === Stage 2: Проверка полей ===
# Project: BikeGarage
from datetime import datetime


def normalize_text(value):
    if value is None:
        return ""
    return str(value).strip()


def normalize_type(value):
    allowed = {"городской", "горный", "шоссейный", "гибрид", "электрический"}
    text = normalize_text(value).lower()
    for candidate in allowed:
        if text == candidate or text.startswith(candidate):
            return candidate
    return ""


def normalize_distance(value):
    text = normalize_text(value)
    if not text:
        return 0
    try:
        return abs(float(text))
    except ValueError:
        return 0


def normalize_date(value):
    formats = ("%Y-%m-%d", "%d.%m.%Y", "%d/%m/%Y", "%m/%d/%Y")
    text = normalize_text(value)
    if not text:
        return None
    for fmt in formats:
        try:
            return datetime.strptime(text, fmt).date()
        except ValueError:
            continue
    return None


def validate_name(value):
    name = normalize_text(value)
    if not name:
        return "Название не может быть пустым."
    if len(name) > 60:
        return "Название слишком длинное (максимум 60 символов)."
    return None


def validate_type(value):
    normalized = normalize_type(value)
    if not normalized:
        return "Не удалось распознать тип велосипеда. Допустимые значения: городской, горный, шоссейный, гибрид, электрический."
    return None


def validate_distance(value):
    distance = normalize_distance(value)
    if distance < 0:
        return "Пробег не может быть отрицательным."
    return None


def validate_service_date(value):
    date = normalize_date(value)
    if not date:
        return "Не удалось распознать дату обслуживания. Форматы: ГГГГ-ММ-ДД, ДД.ММ.ГГГГ или ДД/ММ/ГГГГ."
    return None
