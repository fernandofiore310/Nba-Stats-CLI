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