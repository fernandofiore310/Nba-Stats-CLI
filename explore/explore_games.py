import time

from nba_stats_cli.client import Client
from nba_stats_cli.db import close_connection, connect, record_games
from nba_stats_cli.transform import games_params
from nba_stats_cli.load import load_games

# Temporada 2024-2025 teve 1320 jogos, segundo o gemini. Ja 2025=2026 teve 1322. Um total de 2642 jogos.
# Considerando que a cada request vou pegar 100 jogos, vou precisar de 27 request para pegar todos, ou seja, 27 paginas.
# Considerando que tenho 5 request por minuto, vou demorar um total aproximado de 6 minutos para pegar todos.

if __name__ == "__main__":
    conn = connect()
    client = Client()
    seasons = [2024, 2025]

    inicio = time.monotonic()
    load_games(conn=conn, client=client, seasons=seasons)
    fim = time.monotonic()
    print(f"Tempo total: {fim-inicio}s")

    close_connection(conn=conn)
        
# Tempo total: 304.47313172400027s
# Numero de jogos: 2643
# Esses foram os resultados dos prints do terminal. O tempo ficou quase um minuto abaixo do que eu esperava.
# No entanto, o numero de jogos foi muito proximo. O gemini e a API diferem por 1 jogo. Sera que vale ir atras de que jogo eh esse?
# Podia ter contado o numero de iteracoes do loop while para ver quantos requests foram feitos. Nao pensei nisso antes de rodar.
    