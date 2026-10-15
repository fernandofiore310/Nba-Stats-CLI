-- Rodar no terminal: sqlite3 data/nba.db < sql/checks.sql

PRAGMA foreign_key_check;

SELECT * FROM teams;