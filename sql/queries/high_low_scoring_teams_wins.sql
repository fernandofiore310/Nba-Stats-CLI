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

SELECT
t.full_name,
t.abbreviation,
COUNT(g.id) AS home_wins
FROM games g
JOIN teams t ON g.home_team_id=t.id
WHERE g.home_team_score > g.visitor_team_score AND g.season = 2025 AND g.postseason IS FALSE
GROUP BY t.id
ORDER BY home_wins DESC
;

SELECT
t.full_name,
t.abbreviation,
COUNT(g.id) AS visitor_wins
FROM games g
JOIN teams t ON g.visitor_team_id=t.id
WHERE g.home_team_score < g.visitor_team_score AND g.season = 2025 AND g.postseason IS FALSE
GROUP BY t.id
ORDER BY visitor_wins DESC
;

SELECT
t.full_name,
t.abbreviation,
SUM(g.home_team_score) total_points_home
FROM games g
JOIN teams t ON g.home_team_id=t.id
WHERE g.season = 2025 AND g.postseason IS FALSE
GROUP BY t.id
ORDER BY total_points_home DESC
;

SELECT
t.full_name,
t.abbreviation,
SUM(g.visitor_team_score) total_points_visitor
FROM games g
JOIN teams t ON g.visitor_team_id=t.id
WHERE g.season = 2025 AND g.postseason IS FALSE
GROUP BY t.id
ORDER BY total_points_visitor DESC
;

