-- Colleges que mais tiveram picks top 5 primeiro round.
-- Tempo: 7min
-- Esperado (na mão, antes de rodar): Nao sei. O unico jeito de saber o que esperar eh pesquisar
-- Conferência: Acredito que bateu, baseado no meu conhecimento de basquete. Pesquisei na internet e o resultado eh proximo, mas nao igual. Acredito que pode ser da base a diferenca, ou considerando o draft mais recente.
-- Consulta: Nenhuma
-- (explicação, quando o exercício pedir)

SELECT 
p.college,
COUNT(p.id) top_5_picks,
RANK() OVER (
    ORDER BY COUNT(p.id) DESC
) AS position
FROM players p
WHERE p.college IS NOT NULL AND p.draft_round == 1 AND p.draft_number <= 5
GROUP BY p.college
ORDER BY top_5_picks DESC
LIMIT 20
;

-- Colleges que mais tiveram picks de primeiro round.
SELECT 
p.college,
COUNT(p.id) first_round_picks,
RANK() OVER (
    ORDER BY COUNT(p.id) DESC
) AS position
FROM players p
WHERE p.college IS NOT NULL AND p.draft_round == 1
GROUP BY p.college
ORDER BY first_round_picks DESC
LIMIT 20
;