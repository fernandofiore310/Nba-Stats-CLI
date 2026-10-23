
from sqlite3 import Connection
from typing import Any

from nba_stats_cli.db import create_cursor
from nba_stats_cli.load import load_games, load_players, load_teams


class FakeClientTeams:

    def get_data(self, endpoint: str, params: dict[str, Any], cursor: int) -> dict[str, Any]:
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

    def __init__(self) -> None:
        self.c_list: list[int | None] = []

    def get_data(self, endpoint: str, params: dict[str, Any], cursor: int) -> dict[str, Any]:
        self.c_list.append(cursor)

        d: dict[int, dict[str, Any]] = {0: {'data': [
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
        'next_cursor': 2
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
        }
    }
}
        return d[cursor]

class FakeClientPlayers:

    def __init__(self) -> None:
        self.c_list: list[int | None] = []

    def get_data(self, endpoint: str, params: dict[str, Any], cursor: int) -> dict[str, Any]:
        self.c_list.append(cursor)
        
        d: dict[int, dict[str, Any]] = {0: {
        'data': [
            {
            'id': 101,
            'first_name': 'Anthony',
            'last_name': 'Edwards',
            'position': 'G',
            'height': '6-4',
            'weight': '225',
            'jersey_number': '5',
            'college': 'Georgia',
            'country': 'USA',
            'draft_year': 2020,
            'draft_round': 1,
            'draft_number': 1,
            'team': {
                'id': 18,
                'conference': 'West',
                'division': 'Northwest',
                'city': 'Minnesota',
                'name': 'Timberwolves',
                'full_name': 'Minnesota Timberwolves',
                'abbreviation': 'MIN',
            },
        },
        {
            'id': 102,
            'first_name': 'Zion',
            'last_name': 'Williamson',
            'position': 'F',
            'height': '6-6',
            'weight': '284',
            'jersey_number': '1',
            'college': 'Duke',
            'country': 'USA',
            'draft_year': 2019,
            'draft_round': 1,
            'draft_number': 1,
            'team': {
                'id': 19,
                'conference': 'West',
                'division': 'Southwest',
                'city': 'New Orleans',
                'name': 'Pelicans',
                'full_name': 'New Orleans Pelicans',
                'abbreviation': 'NOP',
            },
        }],
        'meta': {
                'next_cursor': 2
                }
        },
        2: {
        'data': [
            {
            'id': 103,
            'first_name': 'Jalen',
            'last_name': 'Brunson',
            'position': 'G',
            'height': '6-2',
            'weight': '190',
            'jersey_number': '11',
            'college': 'Villanova',
            'country': 'USA',
            'draft_year': 2018,
            'draft_round': 2,
            'draft_number': 33,
            'team': {
                'id': 20,
                'conference': 'East',
                'division': 'Atlantic',
                'city': 'New York',
                'name': 'Knicks',
                'full_name': 'New York Knicks',
                'abbreviation': 'NYK',
            },
        },
        {
            'id': 104,
            'first_name': 'Shai',
            'last_name': 'Gilgeous-Alexander',
            'position': 'G',
            'height': '6-6',
            'weight': '195',
            'jersey_number': '2',
            'college': 'Kentucky',
            'country': 'Canada',
            'draft_year': 2018,
            'draft_round': 1,
            'draft_number': 11,
            'team': {
                'id': 21,
                'conference': 'West',
                'division': 'Northwest',
                'city': 'Oklahoma City',
                'name': 'Thunder',
                'full_name': 'Oklahoma City Thunder',
                'abbreviation': 'OKC',
            },
        }],
            'meta': {
                    'next_cursor': 4
                    }
            },
        4: {
        'data': [
            {
            'id': 105,
            'first_name': 'Paolo',
            'last_name': 'Banchero',
            'position': 'F',
            'height': '',
            'weight': ' ',
            'jersey_number': '5',
            'college': 'Duke',
            'country': 'USA',
            'draft_year': 2022,
            'draft_round': 1,
            'draft_number': 1,
            'team': {
                'id': 22,
                'conference': 'East',
                'division': 'Southeast',
                'city': 'Orlando',
                'name': 'Magic',
                'full_name': 'Orlando Magic',
                'abbreviation': 'ORL',
            },
        },
        ],
        'meta': {
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

    cur = create_cursor(conn=conn_memory)
    res = cur.execute("SELECT COUNT(*) FROM teams")
    assert res.fetchone()[0] == 5

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

def test_load_players(conn_memory: Connection) -> None:
    client_t = FakeClientTeams()
    client_p = FakeClientPlayers()

    load_teams(conn=conn_memory, client=client_t)
    load_players(conn=conn_memory, client=client_p)
    assert client_p.c_list == [0,2,4]
    
    cur = create_cursor(conn=conn_memory)
    res = cur.execute("SELECT COUNT(*) FROM players")
    assert res.fetchone()[0] == 5

    cur = create_cursor(conn=conn_memory)
    res = cur.execute("SELECT height, weight FROM players WHERE id=105")
    assert res.fetchall()[0] == (None, None)

    load_players(conn=conn_memory, client=client_p)

    cur = create_cursor(conn=conn_memory)
    res = cur.execute("SELECT COUNT(*) FROM players")
    assert res.fetchone()[0] == 5