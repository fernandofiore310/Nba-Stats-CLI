from sqlite3 import Connection

from nba_stats_cli.db import record_teams


def test_wins_query(conn_memory: Connection, teams_list: list[tuple[int, str, str, str, str, str, str]]) -> None:
    record_teams(conn=conn_memory,teams=teams_list)

