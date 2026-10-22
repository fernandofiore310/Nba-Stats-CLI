from nba_stats_cli.db import close_connection, connect
from nba_stats_cli.client import Client
from nba_stats_cli.load import load_teams

if __name__ == "__main__":
    conn = connect()
    client = Client()
    nteams = load_teams(conn=conn, client=client)

    #teste para verificar se pegou os 30 times da nba
    #Deixo ele aqui pois nao eh uma regra de carga, mas sim uma expectativa sobre os dados reais da API.
    assert nteams == 30

    close_connection(conn=conn)