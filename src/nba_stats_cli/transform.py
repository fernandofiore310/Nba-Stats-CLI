from typing import Any


def calc_weight(weight: str) -> int:
    w: float = float(int(weight))
    w = w*0.453592
    return int(w)

def calc_height(height: str) -> int:
    lh = height.split('-')
    feet = float(int(lh[0]))
    inch = float(int(lh[1]))
    # print(feet)
    # print(inch)
    h = feet*12 + inch
    h = h * 2.54
    return int(h)

def team_params(dic: dict[str, Any]) -> tuple[int, str, str, str, str, str, str]:
    tupla = (dic['id'], 
            dic['conference'], 
            dic['division'],
            dic['city'],
            dic['name'],
            dic['full_name'],
            dic['abbreviation'] 
            )
    return tupla

def player_params(dic: dict[str, Any]) -> tuple[int, str, str, str, int, int, str, str, str, int | None, int | None, int | None, int]:

    weight = calc_weight(dic['weight'])
    team_id = dic['team']['id']
    height = calc_height(dic['height'])

    tupla = (dic['id'], 
            dic['first_name'], 
            dic['last_name'],
            dic['position'],
            height,
            weight,
            dic['jersey_number'],
            dic['college'],
            dic['country'],
            dic['draft_year'],
            dic['draft_round'],
            dic['draft_number'],
            team_id
            )
    return tupla
