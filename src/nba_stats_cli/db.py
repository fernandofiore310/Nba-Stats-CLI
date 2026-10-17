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

def close_connection(conn: Connection) -> None:
    conn.close()

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

def record_games(conn: Connection, games: list[tuple[int, str, int, bool, bool, int, int, int, int, int, int, int | None, int | None, int | None, int, int, int, int, int | None, int | None, int | None, str | None, int, int]]) -> None:
    cursor = create_cursor(conn)
    
    try:
        cursor.executemany(
        """
        INSERT INTO games (
            id,
            date,
            season,
            postseason,
            postponed,
            home_team_score,
            visitor_team_score,
            home_q1,
            home_q2,
            home_q3,
            home_q4,
            home_ot1,
            home_ot2,
            home_ot3,
            visitor_q1,
            visitor_q2,
            visitor_q3,
            visitor_q4,
            visitor_ot1,
            visitor_ot2,
            visitor_ot3,
            ist_stage,
            home_team_id,
            visitor_team_id
        )
        VALUES (
            ?, ?, ?, ?, ?, ?, ?, ?,
            ?, ?, ?, ?, ?, ?, ?, ?,
            ?, ?, ?, ?, ?, ?, ?, ?
        )
        ON CONFLICT (id)
        DO UPDATE SET
            date = EXCLUDED.date,
            season = EXCLUDED.season,
            postseason = EXCLUDED.postseason,
            postponed = EXCLUDED.postponed,
            home_team_score = EXCLUDED.home_team_score,
            visitor_team_score = EXCLUDED.visitor_team_score,
            home_q1 = EXCLUDED.home_q1,
            home_q2 = EXCLUDED.home_q2,
            home_q3 = EXCLUDED.home_q3,
            home_q4 = EXCLUDED.home_q4,
            home_ot1 = EXCLUDED.home_ot1,
            home_ot2 = EXCLUDED.home_ot2,
            home_ot3 = EXCLUDED.home_ot3,
            visitor_q1 = EXCLUDED.visitor_q1,
            visitor_q2 = EXCLUDED.visitor_q2,
            visitor_q3 = EXCLUDED.visitor_q3,
            visitor_q4 = EXCLUDED.visitor_q4,
            visitor_ot1 = EXCLUDED.visitor_ot1,
            visitor_ot2 = EXCLUDED.visitor_ot2,
            visitor_ot3 = EXCLUDED.visitor_ot3,
            ist_stage = EXCLUDED.ist_stage,
            home_team_id = EXCLUDED.home_team_id,
            visitor_team_id = EXCLUDED.visitor_team_id;
        """,
        games,
        )

        conn.commit()

    except sqlite3.Error:
        print("Insercao nao deu certo!")
        conn.rollback()
        raise