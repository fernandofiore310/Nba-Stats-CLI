from typing import Any

from nba_stats_cli.transform import calc_height, calc_weight, team_params, player_params

if __name__ == "__main__":

    dic_tatum = {'data': [{'id': 434, 'first_name': 'Jayson', 'last_name': 'Tatum', 'position': 'F', 'height': '6-8', 'weight': '229', 'jersey_number': '0', 'college': 'Duke', 'country': 'USA', 'draft_year': 2017, 'draft_round': 1, 'draft_number': 3, 'team': {'id': 2, 'conference': 'East', 'division': 'Atlantic', 'city': 'Boston', 'name': 'Celtics', 'full_name': 'Boston Celtics', 'abbreviation': 'BOS'}}], 'meta': {'per_page': 25}}
    tatum = dic_tatum['data'][0]

    dic_j = {'data': [{'id': 434, 'first_name': 'Jayson', 'last_name': 'Tatum', 'position': 'F', 'height': None, 'weight': None, 'jersey_number': None, 'college': None, 'country': 'USA', 'draft_year': None, 'draft_round': None, 'draft_number': None, 'team': {'id': 2, 'conference': 'East', 'division': 'Atlantic', 'city': 'Boston', 'name': 'Celtics', 'full_name': 'Boston Celtics', 'abbreviation': 'BOS'}}], 'meta': {'per_page': 25}}
    j = dic_j['data'][0]
    
    altura = calc_height(tatum['height'])
    altura2 = calc_height("7-0")
    altura3 = calc_height("6-11")
    altura4 = calc_height(None)
    assert altura == 203
    assert altura2 == 213
    assert altura3 == 211
    assert altura4 is None

    peso = calc_weight(tatum['weight'])
    peso2 = calc_weight(None)
    assert peso == 104
    assert peso2 is None

    assert team_params(tatum) == (2, 'East', 'Atlantic', 'Boston', 'Celtics', 'Boston Celtics', 'BOS')
    
    assert player_params(tatum) == (434, 'Jayson', 'Tatum', 'F', 203, 104, '0', 'Duke', 'USA', 2017, 1, 3, 2)