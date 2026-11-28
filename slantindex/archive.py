"""Store daily schedule projections and build a consistent aggregate export."""

from dataclasses import astuple
from datetime import date, datetime, timedelta, timezone
import hashlib
import json
from pathlib import Path
import sqlite3

from .schedule import STATION, covered_seconds, day_bounds, parse_day


def connect(path: Path) -> sqlite3.Connection:
    db = sqlite3.connect(path)
    db.row_factory = sqlite3.Row
    try:
        db.execute("PRAGMA foreign_keys = ON")
        version = db.execute("PRAGMA user_version").fetchone()[0]
        if version == 0:
            sql = Path(__file__).with_name("migrations") / "001_schedule.sql"
            db.executescript(sql.read_text())
        elif version != 1:
            raise ValueError(f"Unsupported database schema {version}")
    except Exception:
        db.close()
        raise
    return db


def import_day(db, day: date, body: bytes, url: str):
    slots = [astuple(slot) for slot in parse_day(body, day)]
    digest = hashlib.sha256(json.dumps(slots).encode()).hexdigest()
    keys = (STATION, day.isoformat())
    with db:
        db.execute("BEGIN IMMEDIATE")
        current = db.execute(
            "SELECT projection_hash, source_url FROM schedule_day WHERE station=? AND day=?", keys
        ).fetchone()
        if current and tuple(current) == (digest, url):
            return
        db.execute("""
            INSERT INTO schedule_day VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(station, day) DO UPDATE SET source_url=excluded.source_url,
                projection_hash=excluded.projection_hash, retrieved_at=excluded.retrieved_at
        """, (*keys, url, digest, datetime.now(timezone.utc).isoformat()))
        db.execute("DELETE FROM broadcast WHERE station=? AND day=?", keys)
        db.executemany("""
            INSERT INTO broadcast (station, day, source_id, start_utc, end_utc, show_id, genre, repeat)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, [(*keys, *slot) for slot in slots])


def dates(first: date, last: date):
    if last < first:
        raise ValueError("End date precedes start date")
    for offset in range((last - first).days + 1):
        yield first + timedelta(days=offset)


def snapshot(db, first: date, last: date) -> dict:
    days = []
    with db:
        db.execute("BEGIN")
        for day in dates(first, last):
            station_day = (STATION, day.isoformat())
            record = db.execute(
                "SELECT source_url FROM schedule_day WHERE station=? AND day=?", station_day
            ).fetchone()
            rows = db.execute(
                "SELECT * FROM reviewed_broadcast WHERE station=? AND day=?", station_day
            ).fetchall()
            lower, upper = day_bounds(day)
            starts = [r for r in rows if lower <= r["start_utc"] < upper]
            days.append({
                "date": day.isoformat(), "available": bool(record),
                "source": record[0] if record else None,
                "secondsInDay": upper - lower, "slots": len(starts),
                "repeatSlots": sum(r["repeat"] == 1 for r in starts),
                "unknownRepeatSlots": sum(r["repeat"] is None for r in starts),
                "missingShowId": sum(r["show_id"] is None for r in starts),
                "coveredSeconds": covered_seconds(
                    [(r["start_utc"], r["end_utc"]) for r in rows], lower, upper
                ),
            })
    return {"station": STATION, "from": first.isoformat(), "to": last.isoformat(), "days": days}
