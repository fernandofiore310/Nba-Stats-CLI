import time
from typing import Any

from nba_stats_cli.cliente import get_page


def printa_players(data: list[dict[str, Any]], n: int) -> None:
    for i, player in enumerate(data, start=1):
        print(f"{player['first_name']} {player['last_name']}")
        if i == n: break

def monta_set(data: list[dict[str, Any]]) -> set[int]:
    set1 = set()
    for player in data:
        set1.add(player['id'])
    return set1

if __name__ == "__main__":
    endpoint = "players"
    params: dict[str, Any] = {}
    c1 = 0
    dic = get_page(endpoint=endpoint, params=params, cursor=c1)

    data = dic['data']
    meta = dic['meta']

    n = 10

    printa_players(data=data, n=n)

    set1 = monta_set(data=data)

    c2 = meta['next_cursor']

    time.sleep(13)

    dic2 = get_page(endpoint=endpoint, params=params, cursor=c2)

    data2 = dic2['data']
    
    printa_players(data=data2, n=n)

    set2 = monta_set(data=data2)

    assert set1 & set2 == set()

    

