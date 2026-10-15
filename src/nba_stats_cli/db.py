import sqlite3
from sqlite3 import Connection, Cursor

BANCO = "data/nba.db"

def connect() -> Connection:
    conn = sqlite3.connect(BANCO)
    conn.execute("PRAGMA foreign_keys = ON")

    with open("sql/schema.sql", "r", encoding="utf-8") as f:
        script = f.read()

    conn.executescript(script)

    return conn

def create_cursor(conn: Connection) -> Cursor:
    return conn.cursor()

def record_teams(conn: Connection, teams: list[tuple[int, str, str, str, str, str, str]]) -> None:
    cursor = create_cursor(conn)
    
    try:
        cursor.executemany(
            """
            INSERT INTO teams (id, conference, division, city, name, full_name, abbreviation) 
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT (id) 
            DO UPDATE SET 
            conference = EXCLUDED.conference,
            division = EXCLUDED.division,
            city = EXCLUDED.city,
            name = EXCLUDED.name,
            full_name = EXCLUDED.full_name,
            abbreviation = EXCLUDED.abbreviation;
            """,
            teams,
        )

        conn.commit()

    except sqlite3.Error:
        print("Insercao nao deu certo!")
        conn.rollback()
        raise