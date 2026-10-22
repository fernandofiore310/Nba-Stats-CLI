import time

from nba_stats_cli.client import Client
from nba_stats_cli.db import close_connection, connect
from nba_stats_cli.load import load_players

if __name__ == "__main__":
    conn = connect()
    client = Client()

    inicio = time.monotonic()
    load_players(conn=conn, client=client)
    fim = time.monotonic()
    print(f"Tempo total: {fim-inicio}s")
    
    close_connection(conn=conn)
