-- Quais foram os times que mais fizeram pontos em uma temporada? Quais foram os que menos fizeram pontos? Como isso se relaciona com vitorias em uma temporada?
-- Tempo: 
-- Esperado (na mão, antes de rodar): Usei o thunder 25-26 como exemplo, entao somando as vitorias em casa e fora deveria ser 64 e os pontos 9760.
-- Conferência: Os dois bateram (basketball reference)
-- Consulta: Nenhuma
-- (explicação, quando o exercício pedir)

-- WITH teams_wins AS (
-- t.full_name,
-- t.abbreviation,
-- COUNT(

-- )
-- )

-- SELECT
-- t.full_name,
-- t.abbreviation,
-- COUNT(g.id) AS home_wins
-- FROM games g
-- JOIN teams t ON g.home_team_id=t.id
-- WHERE g.home_team_score > g.visitor_team_score AND g.season = 2025 AND g.postseason IS FALSE
-- GROUP BY t.id
-- ORDER BY home_wins DESC
-- ;

-- SELECT
-- t.full_name,
-- t.abbreviation,
-- COUNT(g.id) AS visitor_wins
-- FROM games g
-- JOIN teams t ON g.visitor_team_id=t.id
-- WHERE g.home_team_score < g.visitor_team_score AND g.season = 2025 AND g.postseason IS FALSE
-- GROUP BY t.id
-- ORDER BY visitor_wins DESC
-- ;

-- SELECT
-- t.full_name,
-- t.abbreviation,
-- SUM(g.home_team_score) total_points_home
-- FROM games g
-- JOIN teams t ON g.home_team_id=t.id
-- WHERE g.season = 2025 AND g.postseason IS FALSE
-- GROUP BY t.id
-- ORDER BY total_points_home DESC
-- ;

-- SELECT
-- t.full_name,
-- t.abbreviation,
-- SUM(g.visitor_team_score) total_points_visitor
-- FROM games g
-- JOIN teams t ON g.visitor_team_id=t.id
-- WHERE g.season = 2025 AND g.postseason IS FALSE
-- GROUP BY t.id
-- ORDER BY total_points_visitor DESC
-- ;

WITH team_games AS (
    SELECT
    t.id as team_id,
    t.full_name,
    t.abbreviation,
    g.season,
    g.date,
    g.home_team_score,
    g.visitor_team_score,
    CASE
        WHEN g.home_team_score > g.visitor_team_score THEN 1
        WHEN g.home_team_score < g.visitor_team_score THEN 0
        ELSE 2
    END AS result
    FROM games g
    JOIN teams t ON g.home_team_id=t.id
    JOIN specific_dates s ON g.season=s.season
    WHERE g.postseason IS FALSE AND g.date <= s.last_reg_season_game_date AND g.id <> s.ist_final_id

    UNION ALL

    SELECT
    t.id as team_id,
    t.full_name,
    t.abbreviation,
    g.season,
    g.date,
    g.home_team_score,
    g.visitor_team_score,
    CASE
        WHEN g.home_team_score > g.visitor_team_score THEN 0
        WHEN g.home_team_score < g.visitor_team_score THEN 1
        ELSE 2
    END AS result
    FROM games g
    JOIN teams t ON g.visitor_team_id=t.id
    JOIN specific_dates s ON g.season=s.season
    WHERE g.postseason IS FALSE AND g.date <= s.last_reg_season_game_date AND g.id <> s.ist_final_id
    ORDER BY g.date
)

SELECT 
full_name,
COUNT(team_id)
FROM team_games
WHERE season = 2024
GROUP BY team_id
HAVING COUNT(team_id) > 82
;