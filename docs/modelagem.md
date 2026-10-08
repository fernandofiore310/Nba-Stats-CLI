## Leitura da API

### Quais campos cada um dos três devolve?
**Teams:** devolve uma lista com todos os times da liga. Cada time possui parametros como id, conferencia, divisao, nome, cidade, e outros. Da para filtrar o resultado a partir dos query parameters division e conference, onde da para pegar os times da divisao/conferencia especifica, alem de poder filtrar pelo id para pegar de um time especifico.
**Players:** devolve uma lista com todos os jogadores da liga. Cada jogador possui parametros como nome e sobrenome, posicao, altura, peso, nacionalidade, numero da camisa, peso, time atual, entre outros. Da para filtrar os resultados usando parametros como nome, sobrenome, ids, pagina de resultado e cursor.
**Games:** devolve uma lista com todos os jogos da liga desde o ano 1946, incluindo jogos que estao acontecendo. Esse endpoint possuem parametros como status, quarto, tempo de jogo, entre outros. Alem disso, cada jogo possui parametros como data, temporada, resultado, pontos, pontos do time da casa e visitante, entre outros. Da para filtrar os resultados usando alguns parametros como temporada, datas, times, e outros. Um ponto importante eh que cada jogo possui os parametros home team e visiting team.

### Quais campos ligam uma entidade a outra? Em que formato eles vêm: só o id, ou o objeto inteiro aninhado?
Como foi discutido, os jogadores possuem os times que jogam atualmente e os jogos possuem os dois times que se enfrentaram naquele jogo especifico. Vale ressaltar que ambos os casos sao interligados com o objeto inteiro aninhado.

### O jogador vem com o time atual ou com o histórico de times? O que isso muda na sua pergunta sobre altura e pontos?
O jogador vem apenas com o time atual, sem seu historico. Isso muda algumas analises pois, por mais que eu tenha acesso a todos os jogos desde 1946, caso eu queria relacionar a altura media dos jogadores de um time com seus resultados, eu so poderia validar usando a temporada atual da API, pois como so tenho o time atual dos jogadores, ia conseguir fazer essa relacao.

### Como a API define uma temporada? Um jogo de janeiro de 2025 pertence a qual?
A season na NBA comecam em uma ano e terminam no outro. A API considera, por exemplo, a temporada 24-25 como temporada 2024. Logo, um jogo em janeiro de 2025 eh considerado um jogo da temporada 2024.

## Modelagem

### M1. O desenho
**Teams:** 

Meu projeto vai usar as seguintes colunas para a tabela Teams:

- id
- conference
- division
- city
- name
- full_name
- abbreviation

**Players:** 

Meu projeto vai usar as seguintes colunas para a tabela Players:

- id
- first_name
- last_name
- position
- height
- weight
- jersey_number
- college
- country
- draft_year
- draft_round
- draft_number
- team_id (possui o id do time atual que este jogador joga)

**Games:** 

Meu projeto vai usar as seguintes colunas para a tabela Games:

- id
- date
- season
- postseason
- postponed
- home_team_score
- visitor_team_score
- home_q1
- home_q2
- home_q3
- home_q4
- home_ot1
- home_ot2
- home_ot3
- (o vistor tera as suas colunas de cada quarto e prorrogacao tambem)
- ist_stage
- home_team_id
- visitor_team_id

Alguns pontos de consideracao: (1) estou em certa duvida quando a quais temporadas usar. Ao mesmo tempo que apenas a atual serve para fazer analises com jogadores, pegando todas abre portas para comparar jogos de diferentes temporadas. (2) Acredito que ambos os times de um jogo vao apontar para a mesma tabela. Penso que isso nao deve gerar problemas, considerando que uso apenas o id dos times na tabela de Games.

**Decisao por Escrito**
Acredito que vou usar os mesmo ids da API. Digo isso pois, caso eu estivesse grando os ids e caso eu baixe o dado mais de uma vez, eu vou precisar criar o id novamente, ou seja, eu precisaria rodar o arquivo sql toda vez, o que acredito que seja um problema.

### M4. As perguntas que o banco precisa responder
Quais foram os times que mais fizeram pontos em uma temporada? E vitorias

Qual a altura media dos jogadores dos times que mais venceram/perderam? E dos que mais/menos pontuaram?

Evolucao de pontos ao longo dos jogos das ultimas 20 temporadas.

**Perguntas extras a se responder**

Comparacao de pontos em jogos de temporada regular contra postseason.

Colleges com mais jogadores atualmente.

Colleges que mais tiveram picks top 5 primeiro round.

Dos jogadores atuais, quantos sao de cada classe de draft?

Quais conferencias venceram mais jogos nos ultimos 10/25 anos? E divisoes?

Evolucao de jogos que foram para prorrogacao ao longo dos anos.

Nos playoffs tem uma % maior de jogos que vao para a prorrogacao do que na temporada regular? 

Jogar dentro de casa faz a diferenca nos playoffs? Calcular o aproveitamento dos times que jogaram em casa nos playoffs nos ultimos anos.