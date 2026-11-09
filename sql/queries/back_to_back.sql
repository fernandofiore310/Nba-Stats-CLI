-- Pegar todos os jogos de cada time
-- Ver os dias entre cada jogo
-- Pegar apenas os jogos onde os dias entre o jogo = 1
-- Ver o aproveitamento da equipe nesses jogos
-- Depois, talvez fazer outra query para ver o aproveitamento em jogos que nao sao back to back

WITH team_games AS (
    SELECT
    g.id game_id,
    t.id team_id,
    g.date,
    t.full_name,
    g.home_team_score points_scored,
    CASE
        WHEN g.home_team_score > g.visitor_team_score THEN 1
        WHEN g.home_team_score < g.visitor_team_score THEN 0
        ELSE NULL
    END AS result
    FROM games g 
    JOIN teams t ON g.home_team_id=t.id
    JOIN specific_dates s ON g.season=s.season

    UNION ALL

    SELECT
    g.id game_id,
    t.id team_id,
    g.date,
    t.full_name,
    g.visitor_team_score points_scored,
    CASE
        WHEN g.home_team_score < g.visitor_team_score THEN 1
        WHEN g.home_team_score > g.visitor_team_score THEN 0
        ELSE NULL
    END AS result
    FROM games g 
    JOIN teams t ON g.visitor_team_id=t.id
    JOIN specific_dates s ON g.season=s.season
),
games_days AS (
    SELECT
    game_id,
    team_id,
    date,
    full_name,
    result,
    julianday(date) - julianday(
        LAG(date) OVER (
            PARTITION BY team_id
            ORDER BY date
        )
    ) days_between_games
    FROM team_games
    ORDER BY date
),
back_to_back_teams_games AS (
    SELECT
    *
    FROM
    games_days
    WHERE days_between_games <= 1
),
back_to_back_maths AS (
    SELECT
    team_id,
    full_name,
    SUM(result) OVER (
        PARTITION BY team_id
        ORDER BY date
    ) back_to_back_wins,
    COUNT(result) OVER (
        PARTITION BY team_id
        ORDER BY date
    ) back_to_back_games
    FROM 
    back_to_back_teams_games
    GROUP BY team_id
)

-- SELECT
-- *
-- FROM 
-- back_to_back_teams_games
-- ;

SELECT
full_name,
back_to_back_wins / back_to_back_games back_to_back_win_pct
FROM back_to_back_maths
ORDER BY back_to_back_win_pct DESC
;
