
import sqlite3

def setup_db():
    conn = sqlite3.connect("crypto.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS CRYPTO (
            ID          INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME        TEXT,
            SYMBOL      TEXT,
            PRICE       REAL,
            CHANGE_24HR REAL,
            FETCHED_AT  TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS NEWS (
            ID          INTEGER PRIMARY KEY AUTOINCREMENT,
            HEADLINE    TEXT,
            SCRAPED_AT  TEXT
        )
    """)

    conn.commit()
    conn.close()