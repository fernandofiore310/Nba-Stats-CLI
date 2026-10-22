from sqlite3 import Connection

import pytest

from nba_stats_cli.db import create_cursor, record_teams


@pytest.fixture
def teams_list() -> list[tuple[int, str, str, str, str, str, str]]:
    teams_list = [(2, 'East', 'Atlantic', 'Boston', 'Celtics', 'Boston Celtics', 'BOS'), (4, 'East', 'Southeast', 'Charlotte', 'Hornets', 'Charlotte Hornets', 'CHA'), (6, 'East', 'Southeast', 'Cleveland', 'Cavaliers', 'Cleveland Cavaliers', 'CLE')]
    return teams_list

def test_record_new_teams(conn_memory: Connection, teams_list: list[tuple[int, str, str, str, str, str, str]]) -> None:
    record_teams(conn=conn_memory,teams=teams_list)
    cur = create_cursor(conn=conn_memory)
    res = cur.execute("SELECT COUNT(*) FROM teams")
    assert res.fetchone()[0] == 3

def test_record_same_teams(conn_memory: Connection, teams_list: list[tuple[int, str, str, str, str, str, str]]) -> None:
    record_teams(conn=conn_memory,teams=teams_list)
    cur = create_cursor(conn=conn_memory)
    res = cur.execute("SELECT COUNT(*) FROM teams")
    assert res.fetchone()[0] == 3

    teams_list2 = [(2, 'East', 'Atlantic', 'Boston', 'Celtics', 'Boston Celtics', 'BOS'), (4, 'East', 'Southeast', 'New Orleans', 'Hornets', 'New Orleans Hornets', 'NOH'), (6, 'East', 'Southeast', 'Cleveland', 'Cavaliers', 'Cleveland Cavaliers', 'CLE')]
    record_teams(conn=conn_memory,teams=teams_list2)
    cur = create_cursor(conn=conn_memory)
    res = cur.execute("SELECT COUNT(*) FROM teams")
    assert res.fetchone()[0] == 3
    
    cur = create_cursor(conn=conn_memory)
    res = cur.execute("SELECT city, full_name, abbreviation FROM teams WHERE id=4")
    assert res.fetchone() == ('New Orleans', 'New Orleans Hornets', 'NOH')