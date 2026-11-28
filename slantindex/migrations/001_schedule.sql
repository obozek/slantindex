BEGIN IMMEDIATE;
CREATE TABLE schedule_day (
    station TEXT NOT NULL,
    day TEXT NOT NULL,
    source_url TEXT NOT NULL,
    projection_hash TEXT NOT NULL,
    retrieved_at TEXT NOT NULL,
    PRIMARY KEY (station, day)
);
CREATE TABLE broadcast (
    station TEXT NOT NULL,
    source_id INTEGER NOT NULL,
    day TEXT NOT NULL,
    start_utc INTEGER NOT NULL,
    end_utc INTEGER NOT NULL CHECK (end_utc > start_utc),
    show_id INTEGER,
    genre TEXT,
    repeat INTEGER CHECK (repeat IN (0, 1)),
    PRIMARY KEY (station, day, source_id),
    FOREIGN KEY (station, day) REFERENCES schedule_day(station, day)
);
CREATE INDEX broadcast_by_day ON broadcast(station, day);
-- Preserve an editor's decision if a slot disappears and returns on refresh.
CREATE TABLE repeat_correction (
    station TEXT NOT NULL,
    source_id INTEGER NOT NULL,
    repeat INTEGER NOT NULL CHECK (repeat IN (0, 1)),
    reason TEXT NOT NULL CHECK (length(trim(reason)) > 0),
    source_url TEXT NOT NULL,
    PRIMARY KEY (station, source_id)
);
CREATE VIEW reviewed_broadcast AS
SELECT b.station, b.day, b.source_id, b.start_utc, b.end_utc, b.show_id, b.genre,
       coalesce(c.repeat, b.repeat) AS repeat
FROM broadcast AS b LEFT JOIN repeat_correction AS c USING (station, source_id);
PRAGMA user_version = 1;
COMMIT;
