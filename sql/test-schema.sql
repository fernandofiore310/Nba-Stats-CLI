PRAGMA foreign_keys = ON;

INSERT INTO teams VALUES
 (1,'East','Southeast', 'Atlanta', 'Hawks', 'Atlanta Hawks', 'ATL'),
 (2,'East','Central', 'Milwaulkee', 'Bucks', 'Milwaulkee', 'MIL');

INSERT INTO games VALUES
(15907925, '2025-01-01', 2024, FALSE, FALSE, 110, 108, 24, 35, 25, 26, NULL, NULL, NULL, 25, 29, 27, 27, NULL, NULL, NULL, NULL, 2, 1);

INSERT INTO games (id, date, season, postseason, postponed, home_team_score, visitor_team_score, home_q1, home_q2, home_q3, home_q4, home_ot1, home_ot2, home_ot3, visitor_q1, visitor_q2, visitor_q3, visitor_q4, visitor_ot1, visitor_ot2, visitor_ot3, ist_stage, home_team_id, visitor_team_id) VALUES
(15907926, '2025-01-02', FALSE, FALSE, 110, 108, 24, 35, 25, 26, NULL, NULL, NULL, 25, 29, 27, 27, NULL, NULL, NULL, NULL, 2, 1);

INSERT INTO games (id, date, season, postseason, postponed, home_team_score, visitor_team_score, home_q1, home_q2, home_q3, home_q4, home_ot1, home_ot2, home_ot3, visitor_q1, visitor_q2, visitor_q3, visitor_q4, visitor_ot1, visitor_ot2, visitor_ot3, ist_stage, home_team_id, visitor_team_id) VALUES
(15907927, '2025-01-03', 2024, FALSE, FALSE, -110, 108, 24, 35, 25, 26, NULL, NULL, NULL, 25, 29, 27, 27, NULL, NULL, NULL, NULL, 2, 1);

INSERT INTO games (id, date, season, postseason, postponed, home_team_score, visitor_team_score, home_q1, home_q2, home_q3, home_q4, home_ot1, home_ot2, home_ot3, visitor_q1, visitor_q2, visitor_q3, visitor_q4, visitor_ot1, visitor_ot2, visitor_ot3, ist_stage, home_team_id, visitor_team_id) VALUES
(15907928, '2025-01-04', 2024, FALSE, FALSE, 110, 108, 24, 35, 25, 26, NULL, NULL, NULL, 25, 29, 27, 27, NULL, NULL, NULL, NULL, 2, 3);

-- Antes de rodar: acredito que os tres vao dar erro.
