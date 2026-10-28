"""
Python practice: 2026-10-27

Six small functions about a music library, getting harder as you go.
Replace each `raise NotImplementedError` with your code.

Run the checks:   python3 exercises.py
Each exercise prints PASS, FAIL (with what went wrong) or TODO.
"""

import sqlite3
from pathlib import Path

# Sample data used by the checks. Each track is a dict.
TRACKS = [
    {"name": "Back In Black", "artist": "AC/DC", "genre": "Rock", "ms": 255000},
    {"name": "Thunderstruck", "artist": "AC/DC", "genre": "Rock", "ms": 292000},
    {"name": "So What", "artist": "Miles Davis", "genre": "Jazz", "ms": 562000},
    {"name": "Blue in Green", "artist": "Miles Davis", "genre": "Jazz", "ms": 337000},
    {"name": "Smells Like Teen Spirit", "artist": "Nirvana", "genre": "Rock", "ms": 301000},
    {"name": "Come As You Are", "artist": "Nirvana", "genre": "Rock", "ms": 219000},
    {"name": "Lithium", "artist": "Nirvana", "genre": "Rock", "ms": 257000},
    {"name": "Take Five", "artist": "Dave Brubeck", "genre": "Jazz", "ms": 324000},
    {"name": "Clair de Lune", "artist": "Debussy", "genre": "Classical", "ms": 300000},
]


# Ex1 (strings, integer division)
# Convert milliseconds to "m:ss". Seconds always have 2 digits.
#   format_duration(255000) -> "4:15"
#   format_duration(65000)  -> "1:05"
# Hint: // and % are your friends. f"{x:02d}" pads a number to 2 digits.
def format_duration(ms):
    total_seconds = ms // 1000
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return f"{minutes}:{seconds:02d}"

# Ex2 (loops, dictionaries)
# Count how many tracks each genre has.
#   count_by_genre(TRACKS) -> {"Rock": 5, "Jazz": 3, "Classical": 1}
def count_by_genre(tracks):
    counts = {}
    for track in tracks:
        genre = track["genre"]
        counts[genre] = counts.get(genre, 0) + 1
    return counts

# Ex3 (list comprehension)
# Return the names of tracks whose name contains `query`, ignoring case.
#   search(TRACKS, "in") -> ["Back In Black", "Blue in Green"]
def search(tracks, query):
    results = []
    for t in tracks:
        if query.lower() in t["name"].lower():
            results.append(t["name"])
    return results


# Ex4 (sorting with key=)
# Return the top `n` artists by number of tracks, most first, as (artist, count) tuples.
# If two artists have the same count, put them in alphabetical order.
#   top_artists(TRACKS, 2) -> [("Nirvana", 3), ("AC/DC", 2)]
# Hint: sorted(items, key=lambda pair: (-pair[1], pair[0]))
def top_artists(tracks, n):
    counts = {}
    for t in tracks:
        artist = t["artist"]
        counts[artist] = counts.get(artist, 0) + 1
    ranked = sorted(counts.items(), key=lambda pair: (-pair[1], pair[0]))
    return ranked[:n]

# Ex5 (dict of lists, combining earlier exercises)
# Group tracks by artist and return each artist's total running time as "m:ss".
#   artist_runtimes(TRACKS)["AC/DC"] -> "9:07"
# Hint: reuse format_duration.
def artist_runtimes(tracks):
    totals = {}
    for t in tracks:
        artist = t["artist"]
        totals[artist] = totals.get(artist, 0) + t["ms"]

    result = {}
    for artist, ms in totals.items():
        result[artist] = format_duration(ms)
    return result


# Ex6 (Python + SQL, ties back to yesterday)
# Using the Chinook database, return a list of (genre_name, track_count)
# for the `n` genres with the most tracks, most first.
#   top_genres_from_db(3) -> [("Rock", 1297), ("Latin", 579), ("Metal", 374)]
# Hint: it's your Q3 query from yesterday plus LIMIT.
#   conn = sqlite3.connect(DB_PATH)
#   rows = conn.execute("SELECT ... LIMIT ?", (n,)).fetchall()
def top_genres_from_db(n):
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute("""
        SELECT Genre.Name, COUNT(*) AS TrackCount
        FROM Track
        JOIN Genre ON Track.GenreId = Genre.GenreId
        GROUP BY Genre.Name
        ORDER BY TrackCount DESC
        LIMIT ?
    """, (n,)).fetchall()
    conn.close()
    return rows



DB_PATH = Path(__file__).resolve().parent.parent.parent / "sql" / "data" / "chinook.db"



# ---------------------------------------------------------------------------
# Checks: no need to edit below this line.
# ---------------------------------------------------------------------------

def _check(label, fn, cases):
    try:
        for args, expected in cases:
            got = fn(*args)
            if got != expected:
                print(f"FAIL {label}: {fn.__name__}{args!r:.60}\n       expected {expected!r}\n       got      {got!r}")
                return
        print(f"PASS {label}")
    except NotImplementedError:
        print(f"TODO {label}")
    except Exception as e:
        print(f"FAIL {label}: raised {type(e).__name__}: {e}")


if __name__ == "__main__":
    _check("Ex1", format_duration, [((255000,), "4:15"), ((65000,), "1:05"), ((600000,), "10:00"), ((0,), "0:00")])
    _check("Ex2", count_by_genre, [((TRACKS,), {"Rock": 5, "Jazz": 3, "Classical": 1}), (([],), {})])
    _check("Ex3", search, [((TRACKS, "in"), ["Back In Black", "Blue in Green"]),
                           ((TRACKS, "LUNE"), ["Clair de Lune"]), ((TRACKS, "xyz"), [])])
    _check("Ex4", top_artists, [((TRACKS, 2), [("Nirvana", 3), ("AC/DC", 2)]),
                                ((TRACKS, 4), [("Nirvana", 3), ("AC/DC", 2), ("Miles Davis", 2), ("Dave Brubeck", 1)])])
    _check("Ex5", artist_runtimes, [((TRACKS,), {"AC/DC": "9:07", "Miles Davis": "14:59", "Nirvana": "12:57",
                                                 "Dave Brubeck": "5:24", "Debussy": "5:00"})])
    _check("Ex6", top_genres_from_db, [((3,), [("Rock", 1297), ("Latin", 579), ("Metal", 374)])])
