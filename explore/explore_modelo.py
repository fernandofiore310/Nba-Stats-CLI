from typing import Any

from nba_stats_cli.cliente import get_page

if __name__ == "__main__":
    # endpoint = "teams"
    # params: dict[str, Any] = {}
    # c = 0
    # dic = get_page(endpoint=endpoint, params=params, cursor=c)
    # data = dic['data']
    # for i, team in enumerate(data, start=1):
    #     print(team["full_name"])
    #     if i >= 30:
    #         break
    # print(f"Quantidade de times analisados: {i}")

    endpoint = "players"
    # params: dict[str, Any] = {'team_ids': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]}
    # params: dict[str, Any] = {'first_name': 'Jayson', 'last_name': 'Tatum'}
    params: dict[str, Any] = {'player_ids': [400, 401, 402, 403, 404, 405]}
    c = 0
    i = 0
    while i < 1:
        dicp = get_page(endpoint=endpoint, params=params, cursor=c)
        print(dicp)
        data = dicp['data']
        meta = dicp['meta']
        # for p in data:
        #     print(f"Jogador: {p['first_name']} {p['last_name']}, Time: {p['team']['full_name']}")
        # c = meta['next_cursor']
        i+=1