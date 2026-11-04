from sqlite3 import Connection

from nba_stats_cli.db import record_teams
from nba_stats_cli.queries import execute_query


def test_execute_query(conn_memory: Connection, teams_list: list[tuple[int, str, str, str, str, str, str]]) -> None:
    
    record_teams(conn=conn_memory,teams=teams_list)

    script = """
                SELECT
                city,
                name, 
                abbreviation
                FROM teams
             """

    columns, lines = execute_query(conn=conn_memory, script=script)

    assert columns == ["city", "name", "abbreviation"]
    assert lines == [('Boston', 'Celtics', 'BOS'), ('Charlotte', 'Hornets', 'CHA'), ('Cleveland', 'Cavaliers', 'CLE')]
