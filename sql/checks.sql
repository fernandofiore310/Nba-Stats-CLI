-- Rodar no terminal: sqlite3 data/nba.db < sql/checks.sql

PRAGMA foreign_keys = ON;

PRAGMA foreign_key_check;

SELECT COUNT(*) 
FROM teams
;

SELECT COUNT(*) 
FROM players
;

SELECT COUNT(*) 
FROM games
;

SELECT id, full_name 
FROM teams 
WHERE id = 2
;

SELECT first_name, last_name, height, weight
FROM players
WHERE id = 434
;