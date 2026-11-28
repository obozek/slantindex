from datetime import date
import json
from pathlib import Path
import unittest

from slantindex.archive import connect, import_day, snapshot
from slantindex.schedule import day_bounds

DAY = date(2026, 11, 22)
FIXTURE = (Path(__file__).parent / "fixtures" / f"{DAY}.json").read_bytes()


class ScheduleTests(unittest.TestCase):
    def setUp(self):
        self.db = connect(":memory:")
        self.addCleanup(self.db.close)
        self.load()

    def load(self, body=FIXTURE):
        import_day(self.db, DAY, body, "fixture:2026-11-22")

    def summary(self):
        return snapshot(self.db, DAY, DAY)["days"][0]

    def test_schedule_uses_union_clipped_to_requested_day(self):
        day = self.summary()
        self.assertEqual((day["slots"], day["repeatSlots"], day["missingShowId"]), (3, 1, 1))
        self.assertEqual(day["coveredSeconds"], 45 * 60)

    def test_retry_preserves_data_and_correction(self):
        self.db.execute("INSERT INTO repeat_correction VALUES ('cro-plus',12,1,'Reviewed','https://example.org')")
        self.db.commit()
        self.load()
        self.assertEqual(self.summary()["repeatSlots"], 2)
        changed = json.loads(FIXTURE)
        changed["data"].pop()
        self.load(json.dumps(changed).encode())
        self.assertEqual((self.summary()["repeatSlots"], self.summary()["slots"]), (1, 2))

    def test_empty_or_wrong_day_cannot_replace_valid_data(self):
        for body in [b'{"data":[]}', FIXTURE.replace(b"2026-11-22", b"2025-11-22")]:
            with self.assertRaises(ValueError):
                self.load(body)
        self.assertEqual(self.summary()["slots"], 3)

    def test_unknown_and_missing_are_explicit(self):
        changed = json.loads(FIXTURE)
        del changed["data"][0]["repetition"]
        self.load(json.dumps(changed).encode())
        self.assertEqual(self.summary()["unknownRepeatSlots"], 1)
        missing = snapshot(self.db, date(2026, 11, 21), DAY)["days"][0]
        self.assertFalse(missing["available"])
        self.assertIsNone(missing["source"])

    def test_dst_uses_elapsed_seconds(self):
        for day, hours in [(date(2026, 3, 29), 23), (date(2026, 10, 25), 25)]:
            start, end = day_bounds(day)
            self.assertEqual(end - start, hours * 3600)

    def test_conflicting_duplicate_fails_but_identical_duplicate_counts_once(self):
        rows = json.loads(FIXTURE)["data"]
        rows.append(dict(rows[0]))
        self.load(json.dumps({"data": rows}).encode())
        self.assertEqual(self.summary()["slots"], 3)
        rows[-1]["repetition"] = True
        with self.assertRaises(ValueError):
            self.load(json.dumps({"data": rows}).encode())
        self.assertEqual(self.summary()["repeatSlots"], 1)
