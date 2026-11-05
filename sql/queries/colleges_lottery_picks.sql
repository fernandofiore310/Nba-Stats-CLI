-- Colleges que mais tiveram lottery picks.
-- Tempo: 7min
-- Esperado (na mão, antes de rodar): Nao sei. O unico jeito de saber o que esperar eh pesquisar
-- Conferência: Acredito que bateu, baseado no meu conhecimento de basquete. Pesquisei na internet e o resultado eh proximo, mas nao igual. Acredito que pode ser da base a diferenca, ou considerando o draft mais recente.
-- Consulta: Nenhuma
-- (explicação, quando o exercício pedir)

-- Colleges que mais tiveram picks de loteria
SELECT 
p.college,
COUNT(p.id) lottery_picks,
RANK() OVER (
    ORDER BY COUNT(p.id) DESC
) AS rank
FROM players p
WHERE p.college IS NOT NULL AND p.draft_round == 1 AND p.draft_number <= 14
GROUP BY p.college
ORDER BY lottery_picks DESC
LIMIT 20
;