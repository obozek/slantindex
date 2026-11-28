"""Read the non-personal fields of the Czech Radio daily schedule."""

from dataclasses import dataclass
from datetime import date, datetime, time, timedelta
import json
from zoneinfo import ZoneInfo

PRAGUE = ZoneInfo("Europe/Prague")
STATION = "cro-plus"


def source_url(day: date) -> str:
    return f"https://api.rozhlas.cz/data/v2/schedule/day/{day:%Y/%m/%d}/plus.json"


def day_bounds(day: date) -> tuple[int, int]:
    def midnight(value):
        return int(datetime.combine(value, time.min, PRAGUE).timestamp())

    return midnight(day), midnight(day + timedelta(days=1))


@dataclass(frozen=True)
class Slot:
    source_id: int
    start: int
    end: int
    show_id: int | None
    genre: str | None
    repeat: bool | None


def timestamp(value):
    stamp = datetime.fromisoformat(value)
    if stamp.utcoffset() is None:
        raise ValueError("Schedule timestamps must include a UTC offset")
    return int(stamp.timestamp())


def parse_day(body: bytes, day: date) -> list[Slot]:
    rows = json.loads(body)["data"]
    if not isinstance(rows, list) or not rows:
        raise ValueError("Missing or empty daily schedule")
    lower, upper = day_bounds(day)
    slots = {}
    for row in rows:
        start, end = timestamp(row["since"]), timestamp(row["till"])
        if row["station"] != "plus" or start >= upper or end <= lower or end <= start:
            raise ValueError("Slot has the wrong station, day or duration")
        key = row["id"]
        if type(key) is not int or key <= 0:
            raise ValueError("Invalid broadcast ID")
        repeat = row.get("repetition")
        if repeat is not None and type(repeat) is not bool:
            raise ValueError("Invalid repeat flag")
        # Czech Radio uses [] for an absent edition, including some news bulletins.
        show_id = (row.get("edition") or {}).get("id")
        genre = (row.get("type") or {}).get("code")
        if show_id is not None and type(show_id) is not int:
            raise ValueError("Invalid show ID")
        if genre is not None and not isinstance(genre, str):
            raise ValueError("Invalid genre code")
        slot = Slot(key, start, end, show_id, genre, repeat)
        if key in slots and slots[key] != slot:
            raise ValueError(f"Conflicting entries for broadcast {key}")
        slots[key] = slot
    return sorted(slots.values(), key=lambda x: (x.start, x.source_id))


def covered_seconds(intervals, lower: int, upper: int) -> int:
    until = lower
    total = 0
    for start, end in sorted(intervals):
        end = min(upper, end)
        total += max(0, end - max(start, until))
        until = max(until, end)
    return total
