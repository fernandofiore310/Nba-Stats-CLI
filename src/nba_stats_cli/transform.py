from typing import Any

# Arquivo responsavel pela criacao de tuplas a serem usadas no sql, alem de funcoes de conversao de dados da API para a nossa base de dados.

def calc_weight(weight: str | None) -> int | None:
    if weight is None:
        return None
    
    w: float = float(weight)
    w = w*0.453592
    return round(w)

def calc_height(height: str | None) -> int | None:
    if height is None:
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
