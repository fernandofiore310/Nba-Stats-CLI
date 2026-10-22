from typing import Any
from sqlite3 import Connection
from nba_stats_cli.client import ClientProtocol
from nba_stats_cli.db import record_teams, record_games, record_players
from nba_stats_cli.transform import team_params, games_params, player_params

def load_teams(conn: Connection, client: ClientProtocol) -> int:
    endpoint = "teams"
    params: dict[str, Any] = {}
    c = 0

    d = client.get_data(endpoint=endpoint, params=params, cursor=c)

    all_teams = d['data']
    nba_teams = [team for team in all_teams if team['id'] > 0 and team['id'] <= 30]

    nba_teams_tuple_list = []
    for t in nba_teams:
        nba_teams_tuple_list.append(team_params(t))

    record_teams(conn, nba_teams_tuple_list)

    number_of_teams = len(nba_teams_tuple_list)
    return number_of_teams

def load_games(conn: Connection, client: ClientProtocol, seasons: list[int]) -> None:
    endpoint = "games"
    params = {'per_page': 100, 'seasons[]': seasons}
    c = 0

    paginas = 0
    games_list = []

    while c is not None:
        d = client.get_data(endpoint=endpoint, params=params, cursor=c)

        games = d['data']
        for g in games:
            game = games_params(g)
            games_list.append(game)

        meta = d['meta']
        c = meta.get('next_cursor')
        paginas+=1

    record_games(conn=conn, games=games_list)