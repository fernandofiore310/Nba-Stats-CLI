CREATE TABLE IF NOT EXISTS teams (
    id      INTEGER PRIMARY KEY,
    conference    TEXT NOT NULL,
    division  TEXT NOT NULL, 
    city  TEXT NOT NULL,
    name  TEXT NOT NULL,
    full_name  TEXT NOT NULL,
    abbreviation TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS players (
    id      INTEGER PRIMARY KEY,
    first_name    TEXT NOT NULL,
    last_name  TEXT NOT NULL, 
    position  TEXT NOT NULL,
    height  INTEGER NOT NULL,
    weight  INTEGER NOT NULL,
    jersey_number TEXT NOT NULL,
    college TEXT NOT NULL,
    country TEXT NOT NULL,
    draft_year INTEGER,
    draft_round INTEGER,
    draft_number INTEGER,
    team_id INTEGER NOT NULL REFERENCES teams(id)
);

CREATE TABLE IF NOT EXISTS games (
    id      INTEGER PRIMARY KEY,
    date    TEXT NOT NULL,
    season  INTEGER NOT NULL, 
    postseason  BOOLEAN NOT NULL,
    postponed  BOOLEAN NOT NULL,
    home_team_score  INTEGER NOT NULL,
    visitor_team_score INTEGER NOT NULL,
    home_q1 INTEGER NOT NULL,
    home_q2 INTEGER NOT NULL,
    home_q3 INTEGER NOT NULL,
    home_q4 INTEGER NOT NULL,
    home_ot1 INTEGER,
    home_ot2 INTEGER,
    home_ot3 INTEGER,
    visitor_q1 INTEGER NOT NULL,
    visitor_q2 INTEGER NOT NULL,
    visitor_q3 INTEGER NOT NULL,
    visitor_q4 INTEGER NOT NULL,
    visitor_ot1 INTEGER,
    visitor_ot2 INTEGER,
    visitor_ot3 INTEGER,
    ist_stage TEXT,
    home_team_id INTEGER NOT NULL REFERENCES teams(id),
    visitor_team_id INTEGER NOT NULL REFERENCES teams(id),
    CHECK (home_team_id <> visitor_team_id),
    CHECK (home_team_score >= 0 AND visitor_team_score >= 0)
);