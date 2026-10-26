# daily-practice

Small daily exercises, rotating through a different language each day.

| Day | Language |
|---|---|
| Mon | SQL |
| Tue | Python |
| Wed | TypeScript |
| Thu | JavaScript |
| Fri | Something new (Go / Rust) |

Each day gets its own dated folder under the language, e.g. `sql/2026-10-16/`.

## SQL

Uses the [Chinook](https://github.com/lerocha/chinook-database) sample database (a digital music store) in SQLite.

Build the database once:

```bash
sqlite3 sql/data/chinook.db < sql/data/chinook.sql
```

Then run a day's queries:

```bash
cd sql/2026-10-16
sqlite3 -header -column ../data/chinook.db < queries.sql
```
