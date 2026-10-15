import time

from nba_stats_cli.cliente import get_page

# Temporada 2024-2025 teve 1320 jogos, segundo o gemini. Ja 2025=2026 teve 1322. Um total de 2642 jogos.
# Considerando que a cada request vou pegar 100 jogos, vou precisar de 27 request para pegar todos.
# Considerando que tenho 5 request por minuto, vou demorar um total aproximado de 6 minutos para pegar todos.
if __name__ == "__main__":
    endpoint = "games"
    params = {'per_page': 100, 'seasons': [2024, 2025]}
    c = 0
    games_list = []

    inicio = time.monotonic()
    while c is not None:
        d = get_page(endpoint=endpoint, params=params, cursor=c)

        games = d['data']
        for g in games:
            games_list.append(g)

        meta = d['meta']
        c = meta.get('next_cursor')
        print(f"Next_Cursor: {c}")
        
    fim = time.monotonic()
    print(f"Tempo total: {fim-inicio}s")
    print(f"Numero de jogos: {len(games_list)}")

# Tempo total: 304.47313172400027s
# Numero de jogos: 2643
# Esses foram os resultados dos prints do terminal. O tempo ficou quase um minuto abaixo do que eu esperava.
# No entanto, o numero de jogos foi muito proximo. O gemini e a API diferem por 1 jogo. Sera que vale ir atras de que jogo eh esse?
# Podia ter contado o numero de iteracoes do loop while para ver quantos requests foram feitos. Nao pensei nisso antes de rodar.
    