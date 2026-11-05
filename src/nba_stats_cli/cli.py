import argparse
import sys
from typing import Any

from nba_stats_cli.client import Client
from nba_stats_cli.db import close_connection, connect
from nba_stats_cli.load import load_games, load_players, load_teams
from nba_stats_cli.queries import execute_query

paths = {
    "wins_and_scoring": "sql/queries/high_low_scoring_teams_wins.sql",
    "back-to-back": "sql/queries/back_to_back.sql",
    "colleges_lottery_picks": "sql/queries/colleges_lottery_picks.sql"
}

def print_result(columns: list[str], lines: list[tuple[Any, ...]]) -> None:

    widths = []
    
    for i, column in enumerate(columns):
        width = 0
        width = max(len(column), width)
        for line in lines:
            if line[i] is None:
                width = max(len("-"), width)
            else:
                width = max(len(str(line[i])), width)
        widths.append(width)

    print("\n")
    
    header = " | ".join(f"{c:<{int(widths[i])}}" for i, c in enumerate(columns))
    print(f"{header}\n")

    for line in lines:
        row = " | ".join(f"{str(l) if l is not None else '-':<{int(widths[i])}}" for i, l in enumerate(line))
        print(row)

def load_data(args: argparse.Namespace) -> None:
    
    conn = connect()
    client = Client()
    
    if args.table == "teams":

        if args.seasons is not None:
            print("Error: Flag --seasons cannot be used with argument teams")
            sys.exit(1)

        nteams = load_teams(conn=conn, client=client)

        #teste para verificar se pegou os 30 times da nba
        #Deixo ele aqui pois nao eh uma regra de carga, mas sim uma expectativa sobre os dados reais da API.
        assert nteams == 30

    elif args.table == "players":
        if args.seasons is not None:
            print("Error: Flag --seasons cannot be used with argument players")
            sys.exit(1)

        load_players(conn=conn, client=client)

    else:
        if args.seasons ==  None:
            print("Error: Flag --seasons must be used with argument games")
            sys.exit(1)
        
        else:
            seasons = args.seasons

            load_games(conn=conn, client=client, seasons=seasons)
    
    close_connection(conn=conn)

def load_query(args: argparse.Namespace) -> None:

    conn = connect()

    with open(paths[args.data], "r", encoding="utf-8") as f:
        script = f.read()

    columns, lines = execute_query(conn=conn, script=script)
    
    print_result(columns=columns, lines=lines)
    
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
        type=int,
        nargs="+"
    )

    # Adiciona argumento posicional 'data', na chamada de 'query'
    query_parser.add_argument(
        "data",
        choices=[k for k in paths], # unicas 3 opcoes de valor para 'data'
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