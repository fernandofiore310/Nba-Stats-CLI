from typing import Any, Protocol
from sqlite3 import Connection, Cursor
from nba_stats_cli.client import get_page, ClientProtocol
from nba_stats_cli.db import close_connection, connect, record_teams
from nba_stats_cli.transform import team_params

def load_teams(client: ClientProtocol, conn: Connection) -> int:
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
