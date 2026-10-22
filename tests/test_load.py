import pytest

from typing import Any

from sqlite3 import Connection

from nba_stats_cli.load import load_teams

from nba_stats_cli.db import create_cursor

class FakeClient:

    def get_data(self, endpoint: str, params: dict[str, Any], cursor: int | None = None) -> dict[str, Any]:
        d = {'data': [
        {
            'id': 18,
            'conference': 'West',
            'division': 'Northwest',
            'city': 'Minnesota',
            'name': 'Timberwolves',
            'full_name': 'Minnesota Timberwolves',
            'abbreviation': 'MIN',
        },
        {
            'id': 19,
            'conference': 'West',
            'division': 'Southwest',
            'city': 'New Orleans',
            'name': 'Pelicans',
            'full_name': 'New Orleans Pelicans',
            'abbreviation': 'NOP',
        },
        {
            'id': 20,
            'conference': 'East',
            'division': 'Atlantic',
            'city': 'New York',
            'name': 'Knicks',
            'full_name': 'New York Knicks',
            'abbreviation': 'NYK',
        },
        {
            'id': 21,
            'conference': 'West',
            'division': 'Northwest',
            'city': 'Oklahoma City',
            'name': 'Thunder',
            'full_name': 'Oklahoma City Thunder',
            'abbreviation': 'OKC',
        },
        {
            'id': 22,
            'conference': 'East',
            'division': 'Southeast',
            'city': 'Orlando',
            'name': 'Magic',
            'full_name': 'Orlando Magic',
            'abbreviation': 'ORL',
        },
        {
            'id': 31,
            'conference': 'West',
            'division': 'Northwest',
            'city': 'Seattle',
            'name': 'SuperSonics',
            'full_name': 'Seattle SuperSonics',
            'abbreviation': 'SEA',
        },
    ]}
        return d

def test_load_teams(conn_memory: Connection) -> None:
    client = FakeClient()

    n_teams = load_teams(conn=conn_memory, client=client)
    assert n_teams == 5

    cur = create_cursor(conn=conn_memory)
    res = cur.execute("SELECT id, full_name FROM teams")
    assert res.fetchall() ==  [(18, 'Minnesota Timberwolves'), (19, 'New Orleans Pelicans'), (20, 'New York Knicks'), (21, 'Oklahoma City Thunder'), (22, 'Orlando Magic')] 

    n_teams = load_teams(conn=conn_memory, client=client)
    assert n_teams == 5
