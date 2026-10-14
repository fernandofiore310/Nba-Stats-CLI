from typing import Any

from nba_stats_cli.cliente import get_page
from nba_stats_cli.transform import calc_height, calc_weight, player_params

if __name__ == "__main__":

    endpoint = "players"
    params: dict[str, Any] = {'first_name': 'Jayson', 'last_name': 'Tatum'}
    dic1 = get_page(endpoint=endpoint, params=params)
    # print(dic1)
    altura = calc_height(dic1['data'][0]['height'])
    # print(altura)
    assert altura == 203
    peso = calc_weight(dic1['data'][0]['weight'])
    # print(peso)
    assert peso == 103
    assert player_params(dic1['data'][0]) == (434, 'Jayson', 'Tatum', 'F', 203, 103, '0', 'Duke', 'USA', 2017, 1, 3, 2)