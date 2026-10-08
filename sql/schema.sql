DROP TABLE IF EXISTS teams;
DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS games;

CREATE TABLE teams (
    id      INTEGER PRIMARY KEY,
    conference    TEXT NOT NULL,
    division  TEXT NOT NULL, 
    city  TEXT NOT NULL,
    name  TEXT NOT NULL,
    full_name  TEXT NOT NULL,
    abbreviation TEXT NOT NULL
);

CREATE TABLE players (
    id      INTEGER PRIMARY KEY,
    first_name    TEXT NOT NULL,
    last_name  TEXT NOT NULL, 
    position  TEXT NOT NULL,
    height  TEXT NOT NULL,
    weight  TEXT NOT NULL,
    jersey_number TEXT NOT NULL,
    college TEXT NOT NULL,
    country TEXT NOT NULL,
    draft_year INTEGER NOT NULL,
    draft_round INTEGER NOT NULL,
    draft_number INTEGER NOT NULL,
    team_id INTEGER NOT NULL REFERENCES teams(id)
);

CREATE TABLE games (
    id      INTEGER PRIMARY KEY,
    date    TEXT NOT NULL,
    season  INTEGER NOT NULL, 
    postseason  BOOLEAN NOT NULL,
    postponed  BOOLEAN NOT NULL,
    home_team_score  INTEGER NOT NULL,
    visitor_team_score INTEGER NOT NULL,
    home_q1 INTEGER,
    home_q2 INTEGER,
    home_q3 INTEGER,
    home_q4 INTEGER,
    home_ot1 INTEGER,
    home_ot2 INTEGER,
    home_ot3 INTEGER,
    visitor_q1 INTEGER,
    visitor_q2 INTEGER,
    visitor_q3 INTEGER,
    visitor_q4 INTEGER,
    visitor_ot1 INTEGER,
    visitor_ot2 INTEGER,
    visitor_ot3 INTEGER,
    ist_stage TEXT,
    home_team_id INTEGER NOT NULL REFERENCES teams(id),
    visitor_team_id INTEGER NOT NULL REFERENCES teams(id),
    CHECK (home_team_id <> visitor_team_id),
    CHECK (home_team_score AND visitor_team_score >= 0)
);