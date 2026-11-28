"""Import month-sized batches and serialize compact, non-personal archive facts."""
import argparse
import json
import sys
from contextlib import closing
from datetime import date, timedelta
from pathlib import Path
from time import sleep
from urllib.error import HTTPError

from .__main__ import fetch
from .archive import connect, dates, import_day, snapshot
from .schedule import STATION, source_url


def months(first, last):
    while last >= first:
        start = max(first, last.replace(day=1))
        yield start, last
        last = start - timedelta(days=1)


def write_month(db, start, end, directory):
    days = snapshot(db, start, end)["days"]
    result = {}
    for day in days:
        if day["available"]:
            result[day["date"]] = [
                day[key] for key in ("slots", "repeatSlots", "unknownRepeatSlots",
                                     "missingShowId", "coveredSeconds")
            ]
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / f"{start:%Y-%m}.json"
    existing = json.loads(path.read_text()) if path.exists() else {}
    existing.update(result)
    path.write_text(json.dumps(existing, sort_keys=True, indent=None) + "\n")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--from", dest="first", required=True, type=date.fromisoformat)
    parser.add_argument("--to", dest="last", required=True, type=date.fromisoformat)
    parser.add_argument("--db", type=Path, default=Path("build/slantindex.sqlite"))
    parser.add_argument("--out", type=Path, default=Path("data/archive"))
    parser.add_argument("--refresh", action="store_true")
    args = parser.parse_args()
    args.db.parent.mkdir(parents=True, exist_ok=True)
    with closing(connect(args.db)) as db:
        for start, end in months(args.first, args.last):
            for day in dates(start, end):
                if not args.refresh and db.execute("SELECT 1 FROM schedule_day WHERE station=? AND day=?",
                                                  (STATION, day.isoformat())).fetchone():
                    continue
                url = source_url(day)
                try:
                    import_day(db, day, fetch(url), url)
                except HTTPError as exc:
                    if exc.code not in (404, 410):
                        raise
                    print(f"Missing {day} (HTTP {exc.code})", file=sys.stderr)
                except ValueError as exc:
                    print(f"Unusable {day}: {exc}", file=sys.stderr)
                sleep(0.25)
            result = write_month(db, start, end, args.out)
            print("ARCHIVE " + json.dumps(result, separators=(",", ":")), flush=True)


if __name__ == "__main__":
    main()
