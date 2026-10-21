
from nba_stats_cli.transform import (
    calc_height,
    calc_weight,
    games_params,
    player_params,
    team_params,
)

if __name__ == "__main__":

    dic_tatum = {'data': [{'id': 434, 'first_name': 'Jayson', 'last_name': 'Tatum', 'position': 'F', 'height': '6-8', 'weight': '229', 'jersey_number': '0', 'college': 'Duke', 'country': 'USA', 'draft_year': 2017, 'draft_round': 1, 'draft_number': 3, 'team': {'id': 2, 'conference': 'East', 'division': 'Atlantic', 'city': 'Boston', 'name': 'Celtics', 'full_name': 'Boston Celtics', 'abbreviation': 'BOS'}}], 'meta': {'per_page': 25}}
    tatum = dic_tatum['data'][0]

    dic_j = {'data': [{'id': 434, 'first_name': 'Jayson', 'last_name': 'Tatum', 'position': 'F', 'height': None, 'weight': None, 'jersey_number': None, 'college': None, 'country': 'USA', 'draft_year': None, 'draft_round': None, 'draft_number': None, 'team': {'id': 2, 'conference': 'East', 'division': 'Atlantic', 'city': 'Boston', 'name': 'Celtics', 'full_name': 'Boston Celtics', 'abbreviation': 'BOS'}}], 'meta': {'per_page': 25}}
    j = dic_j['data'][0]
    
    altura = calc_height(tatum['height'])
    altura2 = calc_height("7-0")
    altura3 = calc_height("6-11")
    altura4 = calc_height(None)
    altura5 = calc_height(" ")
    altura6 = calc_height("\t")
    assert altura == 203
    assert altura2 == 213
    assert altura3 == 211
    assert altura4 is None
    assert altura5 is None
    assert altura6 is None

    peso = calc_weight(tatum['weight'])
    peso2 = calc_weight(None)
    peso3 = calc_weight(" ")
    peso4 = calc_weight("\t")
    assert peso == 104
    assert peso2 is None
    assert peso3 is None
    assert peso4 is None

    assert team_params(tatum['team']) == (2, 'East', 'Atlantic', 'Boston', 'Celtics', 'Boston Celtics', 'BOS')
    
    assert player_params(tatum) == (434, 'Jayson', 'Tatum', 'F', 203, 104, '0', 'Duke', 'USA', 2017, 1, 3, 2)

    dic_game = {"data": [{"id": 15907925, "date": "2025-01-05", "season": 2024, "status": "Final", "status_state": "final", "period": 4, "time": "Final", "postseason": False, "postponed": False, "home_team_score": 115, "visitor_team_score": 105, "datetime": "2025-01-05T23:00:00.000Z", "home_q1": 29, "home_q2": 34, "home_q3": 28, "home_q4": 24, "home_ot1": None, "home_ot2": None, "home_ot3": None, "home_timeouts_remaining": 2, "home_in_bonus": True, "visitor_q1": 23, "visitor_q2": 25, "visitor_q3": 30, "visitor_q4": 27, "visitor_ot1": None, "visitor_ot2": None, "visitor_ot3": None, "visitor_timeouts_remaining": 2, "visitor_in_bonus": False, "ist_stage": None, "home_team": {"id": 6, "conference": "East", "division": "Central", "city": "Cleveland", "name": "Cavaliers", "full_name": "Cleveland Cavaliers", "abbreviation": "CLE"}, "visitor_team": {"id": 4, "conference": "East", "division": "Southeast", "city": "Charlotte", "name": "Hornets", "full_name": "Charlotte Hornets", "abbreviation": "CHA"}}], "meta": {"next_cursor": 25, "per_page": 25}}

    assert games_params(dic_game['data'][0]) == (15907925, "2025-01-05", 2024, False, False, 115, 105, 29, 34, 28, 24, None, None, None, 23, 25, 30, 27, None, None, None, None, 6, 4)