import argparse

from nba_stats_cli.client import Client
from nba_stats_cli.db import close_connection, connect
from nba_stats_cli.load import load_teams, load_players, load_games
from nba_stats_cli.queries import execute_query

def load_data(args: argparse.Namespace) -> None:
    
    conn = connect()
    client = Client()
    
    if args.table == "teams":
        nteams = load_teams(conn=conn, client=client)

        #teste para verificar se pegou os 30 times da nba
        #Deixo ele aqui pois nao eh uma regra de carga, mas sim uma expectativa sobre os dados reais da API.
        assert nteams == 30

    elif args.table == "players":

        load_players(conn=conn, client=client)

    else:
        seasons = [2024, 2025]

        load_games(conn=conn, client=client, seasons=seasons)
    
    close_connection(conn=conn)

def load_query(args: argparse.Namespace) -> None:

    conn = connect()

    execute_query(conn=conn, args=args)

    close_connection(conn=conn)

def main() -> None:
    
    # Cria parser principal
    parser = argparse.ArgumentParser(
        description="NBA Stats CLI"
    )

    # Permite criar subcomandos/subparsers
    subparsers = parser.add_subparsers(
        dest="commands",
        required=True
    )

    # Cria subparser chamado load
    load_parser = subparsers.add_parser(
        "load",
        help="Load specified argument into the Database"
    )

    # Cria subparser chamado query
    query_parser = subparsers.add_parser(
            "query",
            help="Show the specified query related to the argument passed"
        )

    # Adiciona argumento posicional 'table', na chamada de 'load'
    load_parser.add_argument(
        "table",
        choices=["teams", "players", "games"], # unicas 3 opcoes de valor para 'table'
        help="Name of the table you want to load to the Database (teams, players, games)"
    )

    # Adiciona argumento opcional '--seasons', na chamada de 'load'
    load_parser.add_argument(
        "--seasons",
        help="The specific seasons you want to get games data from",
        type=int
    )

    # Adiciona argumento posicional 'data', na chamada de 'query'
    query_parser.add_argument(
        "data",
        choices=["wins_and_scoring", "back-to-back", "colleges_picks"], # unicas 3 opcoes de valor para 'data'
        help="Name of the data you want to see"
    )

    # Quando o usuario escolher o subcomando 'load' a funcao load_data sera associada a ele.
    load_parser.set_defaults(func=load_data)
    query_parser.set_defaults(func=load_query)

    args = parser.parse_args()
    args.func(args) #Executa uma das funcoes (load_data ou load_query) dependendo do subcomando usado na CLI

    # print(args)

if __name__ == "__main__":
    main()