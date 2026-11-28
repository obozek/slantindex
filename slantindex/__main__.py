import argparse
from contextlib import closing
from datetime import date, datetime, timedelta
import http.client
import json
from pathlib import Path
import sqlite3
import sys
import tempfile
from urllib.error import HTTPError
from urllib.request import Request, urlopen

from .archive import connect, dates, import_day, snapshot
from .schedule import PRAGUE, STATION, source_url


def fetch(url):
    request = Request(url, headers={"Accept": "application/json", "User-Agent": "SlantIndex/0.1"})
    with urlopen(request, timeout=20) as response:
        return response.read()


def main():
    cli = argparse.ArgumentParser(description="Import and summarize the Czech Radio Plus schedule.")
    cli.add_argument("--db", type=Path, default=Path("build/slantindex.sqlite"))
    commands = cli.add_subparsers(dest="command", required=True)
    yesterday = datetime.now(PRAGUE).date() - timedelta(days=1)
    for name, length in [("import", 7), ("export", 30)]:
        p = commands.add_parser(name)
        p.add_argument("--station", choices=[STATION], default=STATION)
        p.add_argument("--from", dest="first", type=date.fromisoformat)
        p.add_argument("--to", dest="last", type=date.fromisoformat, default=yesterday)
        p.set_defaults(length=length)
        if name == "import":
            p.add_argument("--fixtures", type=Path, help="Read YYYY-MM-DD.json files offline")
        else:
            p.add_argument("--out", type=Path, required=True)
    args = cli.parse_args()
    first = args.first or args.last - timedelta(days=args.length - 1)
    if first > args.last or args.last > yesterday:
        cli.error("Choose an inclusive range of completed Prague calendar days")
    if args.command == "export" and not args.db.is_file():
        cli.error("Import a schedule before exporting")
    args.db.parent.mkdir(parents=True, exist_ok=True)
    with closing(connect(args.db)) as db:
        if args.command == "export":
            if args.out.resolve() == args.db.resolve():
                cli.error("Choose an output path distinct from the database")
            result = snapshot(db, first, args.last)
            args.out.parent.mkdir(parents=True, exist_ok=True)
            with tempfile.NamedTemporaryFile(mode="w", dir=args.out.parent, delete=False) as file:
                json.dump(result, file, ensure_ascii=False, indent=2)
                file.write("\n")
            Path(file.name).replace(args.out)
            print(f"Exported {len(result['days'])} days to {args.out}")
            return 0
        failed = False
        for day in dates(first, args.last):
            try:
                if args.fixtures:
                    body = (args.fixtures / f"{day}.json").read_bytes()
                    url = f"fixture:{day}"
                else:
                    url = source_url(day)
                    body = fetch(url)
                import_day(db, day, body, url)
                print(f"{day} imported")
            except HTTPError as exc:
                print(f"{day} failed: HTTP {exc.code}", file=sys.stderr)
                failed = True
                if exc.code == 429 or exc.headers.get("Retry-After"):
                    delay = exc.headers.get("Retry-After", "the next scheduled run")
                    print(f"Stopping the range. Retry after {delay}.", file=sys.stderr)
                    break
            except (OSError, ValueError, KeyError, AttributeError, TypeError,
                    sqlite3.Error, http.client.HTTPException) as exc:
                print(f"{day} failed: {exc}", file=sys.stderr)
                failed = True
        return int(failed)


if __name__ == "__main__":
    raise SystemExit(main())
