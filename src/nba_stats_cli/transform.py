from typing import Any

# Arquivo responsavel pela criacao de tuplas a serem usadas no sql, alem de funcoes de conversao de dados da API para a nossa base de dados.

def calc_weight(weight: str | None) -> int | None:
    if weight is None or weight.strip() == "":
        return None
    
    w: float = float(weight)
    w = w*0.453592
    return round(w)

def calc_height(height: str | None) -> int | None:
    if height is None or height.strip() == "":
        return None
    
    lh = height.split('-')
    feet = float(lh[0])
    inch = float(lh[1])
    h = feet*12 + inch
    h = h * 2.54
    return round(h)

def team_params(team: dict[str, Any]) -> tuple[int, str, str, str, str, str, str]:
    tupla = (team['id'], 
            team['conference'], 
            team['division'],
            team['city'],
            team['name'],
            team['full_name'],
            team['abbreviation'] 
            )
    return tupla

def player_params(dic: dict[str, Any]) -> tuple[int, str, str, str, int | None, int | None, str | None, str | None, str, int | None, int | None, int | None, int]:

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

def games_params(dic: dict[str, Any]) -> tuple[int, str, int, bool, bool, int, int, int, int, int, int, int | None, int | None, int | None, int, int, int, int, int | None, int | None, int | None, str | None, int, int]:
    home_team_id = dic['home_team']['id']
    visitor_team_id = dic['visitor_team']['id']
    
    tupla = (dic['id'], 
            dic['date'], 
            dic['season'],
            dic['postseason'],
            dic['postponed'],
            dic['home_team_score'],
            dic['visitor_team_score'],
            dic['home_q1'],
            dic['home_q2'],
            dic['home_q3'],
            dic['home_q4'],
            dic['home_ot1'],
            dic['home_ot2'],
            dic['home_ot3'],
            dic['visitor_q1'],
            dic['visitor_q2'],
            dic['visitor_q3'],
            dic['visitor_q4'],
            dic['visitor_ot1'],
            dic['visitor_ot2'],
            dic['visitor_ot3'],
            dic['ist_stage'],
            home_team_id,
            visitor_team_id
            )
    return tupla
