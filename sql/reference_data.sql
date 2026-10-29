INSERT INTO specific_dates (season, last_reg_season_game_date, ist_final_id) 
VALUES
(2024, '2025-04-13', 17195500), -- https://www.basketball-reference.com/leagues/NBA_2025_games-april.html
(2025, '2026-04-12', 20377171)  -- https://www.basketball-reference.com/leagues/NBA_2026_games-april.html
ON CONFLICT (season) 
DO UPDATE SET 
last_reg_season_game_date = EXCLUDED.last_reg_season_game_date,
ist_final_id = EXCLUDED.ist_final_id;