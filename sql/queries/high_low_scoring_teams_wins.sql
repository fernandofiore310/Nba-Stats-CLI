-- Quais foram os times que mais fizeram pontos em uma temporada? Quais foram os que menos fizeram pontos? Como isso se relaciona com vitorias em uma temporada?
-- Tempo: 
-- Esperado (na mão, antes de rodar): Usei o thunder 25-26 como exemplo, entao somando as vitorias em casa e fora deveria ser 64 e os pontos 9760.
-- Conferência: Os dois bateram (basketball reference)
-- Consulta: Nenhuma
-- (explicação, quando o exercício pedir)

WITH team_games AS (
    SELECT
    g.id as game_id,
    t.id as team_id,
    t.full_name,
    t.abbreviation,
    g.season,
    g.date,
    g.home_team_score points_scored,
    g.visitor_team_score points_against,
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
    g.id as game_id,
    t.id as team_id,
    t.full_name,
    t.abbreviation,
    g.season,
    g.date,
    g.visitor_team_score points_scored,
    g.home_team_score points_against,
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
),
team_total_games_and_points_season AS (
    SELECT
    season, 
    full_name,
    SUM(result) total_wins,
    SUM(points_scored) total_points_scored,
    SUM(points_against) total_points_against
    FROM team_games
    GROUP BY team_id, season
)

SELECT
season,
full_name,
total_wins,
RANK() OVER (
    PARTITION BY season
    ORDER BY total_wins DESC
) AS rank_wins,
total_points_scored,
total_points_against
FROM team_total_games_and_points_season
ORDER BY season, rank_wins
;