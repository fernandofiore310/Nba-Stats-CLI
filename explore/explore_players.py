import time

from nba_stats_cli.cliente import get_page
from nba_stats_cli.db import close_connection, connect, record_players
from nba_stats_cli.transform import player_params

# Antes de rodar, eu realmente nao sei quantos jogadores esperar, visto que so contei os jogadores com campos nulos.
if __name__ == "__main__":
    endpoint = "players"
    team_ids = list(range(1, 31))
    params = {'per_page': 100, 'team_ids[]': team_ids}
    c = 0
    page = 0
    players_tuples_list = []
    
    inicio = time.monotonic()
    while c is not None:
        d = get_page(endpoint=endpoint, params=params, cursor=c)
        all_players = d['data']
        for player in all_players:
            p = player_params(player)
            players_tuples_list.append(p)

        meta = d['meta']
        c = meta.get('next_cursor')
        print(f"Next_Cursor: {c}")
        page += 1

    fim = time.monotonic()
    print(f"Tempo total: {fim-inicio}s")
    print(f"Numero de jogadores: {len(players_tuples_list)}")
    print(f"Numero de paginas: {page}")

    conn = connect()
    record_players(conn=conn, players=players_tuples_list)
    close_connection(conn=conn)
