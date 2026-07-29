import sqlite3
from pathlib import Path

database = Path("08_BACKUPS/novyra_os.db")

print("=" * 50)
print("NOVYRA Database Verification")
print("=" * 50)

print(f"Database exists: {database.exists()}")

connection = sqlite3.connect(database)

try:
    tables = connection.execute(
        """
        SELECT name
        FROM sqlite_master
        WHERE type='table'
        ORDER BY name
        """
    ).fetchall()

    print("\nTables:")

    for table in tables:
        print(f" - {table[0]}")

finally:
    connection.close()

print("=" * 50)