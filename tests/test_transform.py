from typing import Any

import pytest

from nba_stats_cli.transform import (
    calc_height,
    calc_weight,
    games_params,
    player_params,
    team_params,
)


@pytest.fixture
def team() -> dict[str, Any]:
    team = {'id': 2, 'conference': 'East', 'division': 'Atlantic', 'city': 'Boston', 'name': 'Celtics', 'full_name': 'Boston Celtics', 'abbreviation': 'BOS'}
    return team

@pytest.mark.parametrize(
    "height,expected_height",
    [
        ("6-8", 203),
        ("7-0", 213),
        ("6-11", 211),
        (None, None),
        ("", None),
        (" ", None),
        ("\t", None),
    ],
)
def test_calc_height(height: str | None, expected_height: int) -> None:
    assert (
        calc_height(height=height) == expected_height
    )

@pytest.mark.parametrize(
    "weight,expected_weight",
    [
        ("229", 104),
        (None, None),
        ("", None),
        (" ", None),
        ("\t", None),
    ],
)
def test_calc_weight(weight: str | None, expected_weight: int) -> None:
    assert (
        calc_weight(weight=weight) == expected_weight
    )

def test_team_params(team: dict[str, Any]) -> None:
    assert team_params(team=team) == (2, 'East', 'Atlantic', 'Boston', 'Celtics', 'Boston Celtics', 'BOS')

def test_player_params() -> None:
    real_player = {'id': 434, 'first_name': 'Jayson', 'last_name': 'Tatum', 'position': 'F', 'height': '6-8', 'weight': '229', 'jersey_number': '0', 'college': 'Duke', 'country': 'USA', 'draft_year': 2017, 'draft_round': 1, 'draft_number': 3, 'team': {'id': 2, 'conference': 'East', 'division': 'Atlantic', 'city': 'Boston', 'name': 'Celtics', 'full_name': 'Boston Celtics', 'abbreviation': 'BOS'}}
    fake_player = {'id': 434, 'first_name': 'Jayson', 'last_name': 'Tatum', 'position': 'F', 'height': None, 'weight': None, 'jersey_number': None, 'college': None, 'country': None, 'draft_year': None, 'draft_round': None, 'draft_number': None, 'team': {'id': 2, 'conference': 'East', 'division': 'Atlantic', 'city': 'Boston', 'name': 'Celtics', 'full_name': 'Boston Celtics', 'abbreviation': 'BOS'}}

    assert player_params(real_player) == (434, 'Jayson', 'Tatum', 'F', 203, 104, '0', 'Duke', 'USA', 2017, 1, 3, 2)
    assert player_params(fake_player) == (434, 'Jayson', 'Tatum', 'F', None, None, None, None, None, None, None, None, 2)

def test_game_params() -> None:
    game = {"id": 15907925, "date": "2025-01-05", "season": 2024, "status": "Final", "status_state": "final", "period": 4, "time": "Final", "postseason": False, "postponed": False, "home_team_score": 115, "visitor_team_score": 105, "datetime": "2025-01-05T23:00:00.000Z", "home_q1": 29, "home_q2": 34, "home_q3": 28, "home_q4": 24, "home_ot1": None, "home_ot2": None, "home_ot3": None, "home_timeouts_remaining": 2, "home_in_bonus": True, "visitor_q1": 23, "visitor_q2": 25, "visitor_q3": 30, "visitor_q4": 27, "visitor_ot1": None, "visitor_ot2": None, "visitor_ot3": None, "visitor_timeouts_remaining": 2, "visitor_in_bonus": False, "ist_stage": None, "home_team": {"id": 6, "conference": "East", "division": "Central", "city": "Cleveland", "name": "Cavaliers", "full_name": "Cleveland Cavaliers", "abbreviation": "CLE"}, "visitor_team": {"id": 4, "conference": "East", "division": "Southeast", "city": "Charlotte", "name": "Hornets", "full_name": "Charlotte Hornets", "abbreviation": "CHA"}}
    game_tuple = games_params(game)

    assert game_tuple[0] == 15907925
    assert game_tuple[22] == 6
    assert game_tuple[23] == 4
    assert game_tuple[11] is None
    assert game_tuple[12] is None
    assert game_tuple[13] is None
    assert game_tuple[18] is None
    assert game_tuple[19] is None
    assert game_tuple[20] is None
