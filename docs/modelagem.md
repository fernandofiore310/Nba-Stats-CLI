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

Qual a altura media dos jogadores dos times que mais venceram/perderam? E dos que mais/menos pontuaram? (nao sera possivel sem conseguir distiguir jogadores atuais e antigos)

Evolucao de pontos ao longo dos jogos das ultimas 20 temporadas.

**Perguntas extras a se responder**

Comparacao de pontos em jogos de temporada regular contra postseason.

Colleges com mais jogadores atualmente.

Colleges que mais tiveram picks top 5 primeiro round.

Dos jogadores atuais, quantos sao de cada classe de draft? (nao sera possivel sem conseguir distiguir jogadores atuais e antigos)

Quais conferencias venceram mais jogos nos ultimos 10/25 anos? E divisoes?

Evolucao de jogos que foram para prorrogacao ao longo dos anos.

Nos playoffs tem uma % maior de jogos que vao para a prorrogacao do que na temporada regular? 

Jogar dentro de casa faz a diferenca nos playoffs? Calcular o aproveitamento dos times que jogaram em casa nos playoffs nos ultimos anos.


## Análise dos dados da API

### Como diferenciar apenas os times da NBA
Como foi visto, a base de dados possui 89 times. No entanto, caso voce printe cada um desses times (como fiz no explore/explore_modelo.py) é possível notar que os primeiros 30 times do endpoint teams são exatamente os times da NBA. Logo, vou pegar os times que possuem os ids de 1 a 30.

### Quais jogadores entram
Como dito anteriormente, queria dar um jeito de pegar apenas jogadores atuais, e que jogam na NBA. Entao, o que fiz foi primeiro passar uma lista no params, com os ids de times de 1 a 30, ja que sabemos que esses sao os times da nba. O problema era diferenciar jogadores atuais e antigos. Percebi, brincando com a API, que jogadores que ja se aposentaram, possuem como time, o ultimo time que jogaram. Testei com Darren Collison, e realmente chequei na internet, seu ultimo time foi o Lakers.
O meu proximo passo eh entender como diferenciar jogadores atuais e antigos de um mesmo time. Abaixo, segue uma comparacao do dicionario de resposta de Radja e de Tatum, uma lenda do celtics e um jogador atual da mesma equipe. Literal nao tem nada que distingue eles. Talvez por id seja possivel.

{'data': [{'id': 808, 'first_name': 'Dino', 'last_name': 'Radja', 'position': 'F', 'height': '6-11', 'weight': '225', 'jersey_number': '40', 'college': 'Virtus Roma', 'country': 'Croatia', 'draft_year': 1989, 'draft_round': 2, 'draft_number': 40, 'team': {'id': 2, 'conference': 'East', 'division': 'Atlantic', 'city': 'Boston', 'name': 'Celtics', 'full_name': 'Boston Celtics', 'abbreviation': 'BOS'}}], 'meta': {'per_page': 25}}

{'data': [{'id': 434, 'first_name': 'Jayson', 'last_name': 'Tatum', 'position': 'F', 'height': '6-8', 'weight': '229', 'jersey_number': '0', 'college': 'Duke', 'country': 'USA', 'draft_year': 2017, 'draft_round': 1, 'draft_number': 3, 'team': {'id': 2, 'conference': 'East', 'division': 'Atlantic', 'city': 'Boston', 'name': 'Celtics', 'full_name': 'Boston Celtics', 'abbreviation': 'BOS'}}], 'meta': {'per_page': 25}}

Entrei no site da nba e fui atras da pagina de jogadores (https://www.nba.com/players). Atualmente, eles marcam uma tabela com 623 linhas, que vou considerar 623 jogadores.
Rodei para os jogadores de id 600-605 e vieram apenas jogadores antigos. Depois rodei para jogadres de ids 400-405 e vieram alguns antigos, tipo derrick rose, e outros atuais, tipo dangelo russell. Entao realmente nao sei como posso diferencia-los.

### Quais temporadas escolher
Considerando que, nas temporadas mais atuais, tem 30 times na NBA, e tirando os anos de 2019-2020 e 2011-2012 que tiveram menos jogos, cada time joga 82 jogos (vou considerar apenas temporada regular)
Logo, por temporada, temos 2460 jogos.
Sem considerar playoffs, playin e a final do inseason tournament, apenas para a temporada passada (2025-2026), considerando que posso pegar 100 jogos por requisicao, teria que fazer um total de 25 requisicoes. Como tenho 5 por minuto, isso me levaria cerca de 5 minutos, apenas para pegar os jogos da temporada regular da temporada passada. Acredito que isso possa ser interessante.
Nao sei o que fazer, caso for fazer com todos os jogos, o caso maximo eh apenas da temporada 2025-2026. Quem sabe da para pegar mais dados de outras temporadas recentes, considerando o tempo de 5 minutos para uma temporada (um pouco mais com os jogos que nao considerei).
Nao existe uma maneira de diferenciar jogadores ativos e historicos. Existe um endpoint para pegar os ativos, mas sera necessario pagar o plano para acessa-lo. Quando tentei acessar, deu um 401 falando que nao estou autorizado.

### Revisao do esquema de modelagem
A unica alteracao que fiz foi deixar os colleges e jersey number NOT NULL, visto que jogadores da NBA sempre vao ter esses atributos, atuais e aposentados. E tambem, coloquei as pontuacoes por quartos nos jogos como NOT NULL, visto que como vou trablahar com temporadas atuais, eles sempre vem com valores.
Eu quero trabalhar com polegadas e pounds para altura e peso, visto que essa eh a metrica da NBA. No entanto, nao sei como posso fazer para converte-los para numeros. Se bem que acredito que nao vou precisar, considerando que por conta da limitacao do endpoint de players, eu nao va mais conseguir realizar operacoes com a altura e peso dos jogadores.
Mas, por outro lado, caso eu queira fazer uma media de altura historica (que ainda assim nao faz muito sentido) eu teria que dar um jeito de converter para numeros. A principio vou mudar para INTEGER e fazer uma conversao numerica, mas nao garanto que vou conseguir fazer analises boas com esses valores. Alem disso, a altura ficara em cm e o peso em kg

### INSERT da minha base
INSERT ... ON CONFLICT DO UPDATE
Decidi usar essa, pois acredito que eh a mais tranquila para lidar com erros e problemas. Mesmo que eu adicione um jogador com id especifico, mas dados diferentes, eh so eu rodar de novo, com os dados certos que ele ja arruma.
E isso serve para o caso de insert dos jogos. Por exemplo, quando for inserir os jogos na tabela, vou fazer o mesmo try catch e usar o ON CONFLICT, de modo que, caso a extracao caia na segunda pagina por exemplo, eu rodo de novo, e se der certo, vai apenas atualizar as colunas das linhas que ja estavam na base.