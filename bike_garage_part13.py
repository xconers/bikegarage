# === Stage 13: Статусы записей ===
# Project: BikeGarage
LIFE_CYCLE_STATUS = (
    "new",
    "in_use",
    "under_service",
    "retired",
)

LIFE_CYCLE_TRANSITIONS = {
    "new": ("in_use",),
    "in_use": ("under_service", "retired"),
    "under_service": ("in_use", "retired"),
    "retired": (),
}


def valid_transition(current_status, target_status):
    return target_status in LIFE_CYCLE_TRANSITIONS.get(current_status, ())


def next_status(current_status):
    return LIFE_CYCLE_TRANSITIONS.get(current_status, ())


def is_terminal(status):
    return status in LIFE_CYCLE_TRANSITIONS and not LIFE_CYCLE_TRANSITIONS[status]
