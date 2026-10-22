import pytest

from typing import Any

from sqlite3 import Connection

from nba_stats_cli.load import load_teams, load_games

from nba_stats_cli.db import create_cursor

class FakeClientTeams:

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

class FakeClientGames:

    def __init__(self):
        self.c_list: list[int] = []

    def get_data(self, endpoint: str, params: dict[str, Any], cursor: int | None = None) -> dict[str, Any]:
        self.c_list.append(cursor)

        d = {0: {'data': [
        {
            "id": 0,
            "date": "2025-01-10",
            "season": 2024,
            "status": "Final",
            "status_state": "final",
            "period": 4,
            "time": "Final",
            "postseason": False,
            "postponed": False,
            "home_team_score": 112,
            "visitor_team_score": 108,
            "datetime": "2025-01-10T20:00:00.000Z",
            "home_q1": 28,
            "home_q2": 30,
            "home_q3": 26,
            "home_q4": 28,
            "home_ot1": None,
            "home_ot2": None,
            "home_ot3": None,
            "home_timeouts_remaining": 1,
            "home_in_bonus": True,
            "visitor_q1": 25,
            "visitor_q2": 27,
            "visitor_q3": 29,
            "visitor_q4": 27,
            "visitor_ot1": None,
            "visitor_ot2": None,
            "visitor_ot3": None,
            "visitor_timeouts_remaining": 2,
            "visitor_in_bonus": True,
            "ist_stage": None,
            "home_team": {
                "id": 18,
                "conference": "West",
                "division": "Northwest",
                "city": "Minnesota",
                "name": "Timberwolves",
                "full_name": "Minnesota Timberwolves",
                "abbreviation": "MIN",
            },
            "visitor_team": {
                "id": 19,
                "conference": "West",
                "division": "Southwest",
                "city": "New Orleans",
                "name": "Pelicans",
                "full_name": "New Orleans Pelicans",
                "abbreviation": "NOP",
            },
        },
        {
            "id": 1,
            "date": "2025-01-12",
            "season": 2024,
            "status": "Final",
            "status_state": "final",
            "period": 4,
            "time": "Final",
            "postseason": False,
            "postponed": False,
            "home_team_score": 104,
            "visitor_team_score": 115,
            "datetime": "2025-01-12T23:30:00.000Z",
            "home_q1": 22,
            "home_q2": 28,
            "home_q3": 25,
            "home_q4": 29,
            "home_ot1": None,
            "home_ot2": None,
            "home_ot3": None,
            "home_timeouts_remaining": 2,
            "home_in_bonus": False,
            "visitor_q1": 31,
            "visitor_q2": 26,
            "visitor_q3": 28,
            "visitor_q4": 30,
            "visitor_ot1": None,
            "visitor_ot2": None,
            "visitor_ot3": None,
            "visitor_timeouts_remaining": 3,
            "visitor_in_bonus": True,
            "ist_stage": None,
            "home_team": {
                "id": 20,
                "conference": "East",
                "division": "Atlantic",
                "city": "New York",
                "name": "Knicks",
                "full_name": "New York Knicks",
                "abbreviation": "NYK",
            },
            "visitor_team": {
                "id": 21,
                "conference": "West",
                "division": "Northwest",
                "city": "Oklahoma City",
                "name": "Thunder",
                "full_name": "Oklahoma City Thunder",
                "abbreviation": "OKC",
            },
        },
    ], 'meta': {
        'next_cursor': 2,
        'per_page': 1
        }
    },
    2: {'data': [
        {
            "id": 2,
            "date": "2025-01-15",
            "season": 2024,
            "status": "Final",
            "status_state": "final",
            "period": 4,
            "time": "Final",
            "postseason": False,
            "postponed": False,
            "home_team_score": 98,
            "visitor_team_score": 102,
            "datetime": "2025-01-15T00:00:00.000Z",
            "home_q1": 24,
            "home_q2": 26,
            "home_q3": 22,
            "home_q4": 26,
            "home_ot1": None,
            "home_ot2": None,
            "home_ot3": None,
            "home_timeouts_remaining": 1,
            "home_in_bonus": True,
            "visitor_q1": 27,
            "visitor_q2": 24,
            "visitor_q3": 25,
            "visitor_q4": 26,
            "visitor_ot1": None,
            "visitor_ot2": None,
            "visitor_ot3": None,
            "visitor_timeouts_remaining": 2,
            "visitor_in_bonus": False,
            "ist_stage": None,
            "home_team": {
                "id": 22,
                "conference": "East",
                "division": "Southeast",
                "city": "Orlando",
                "name": "Magic",
                "full_name": "Orlando Magic",
                "abbreviation": "ORL",
            },
            "visitor_team": {
                "id": 18,
                "conference": "West",
                "division": "Northwest",
                "city": "Minnesota",
                "name": "Timberwolves",
                "full_name": "Minnesota Timberwolves",
                "abbreviation": "MIN",
            },
        }
    ], 'meta': {
        'next_cursor': None,
        'per_page': None
        }
    }
}
        return d[cursor]

def test_load_teams(conn_memory: Connection) -> None:
    client = FakeClientTeams()

    n_teams = load_teams(conn=conn_memory, client=client)
    assert n_teams == 5

    cur = create_cursor(conn=conn_memory)
    res = cur.execute("SELECT id, full_name FROM teams")
    assert res.fetchall() ==  [(18, 'Minnesota Timberwolves'), (19, 'New Orleans Pelicans'), (20, 'New York Knicks'), (21, 'Oklahoma City Thunder'), (22, 'Orlando Magic')] 

    n_teams = load_teams(conn=conn_memory, client=client)
    assert n_teams == 5

def test_load_games(conn_memory: Connection) -> None:
    client_t = FakeClientTeams()
    client_g = FakeClientGames()
    seasons = [2025]

    load_teams(conn=conn_memory, client=client_t)
    load_games(conn=conn_memory, client=client_g, seasons=seasons)
    assert client_g.c_list == [0,2]
    
    cur = create_cursor(conn=conn_memory)
    res = cur.execute("SELECT COUNT(*) FROM games")
    assert res.fetchone()[0] == 3

    load_games(conn=conn_memory, client=client_g, seasons=seasons)

    cur = create_cursor(conn=conn_memory)
    res = cur.execute("SELECT COUNT(*) FROM games")
    assert res.fetchone()[0] == 3