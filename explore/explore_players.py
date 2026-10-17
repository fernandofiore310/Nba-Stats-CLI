from nba_stats_cli.cliente import get_page
from nba_stats_cli.db import connect, record_teams, close_connection
from nba_stats_cli.transform import team_params

if __name__ == "__main__":
    endpoint = "players"
    team_ids = list(range(1, 31))
    params = {'per_page': 100, 'team_ids': team_ids}
    c = 0
    page = 0
    null_players = 0

    while c is not None:
        d = get_page(endpoint=endpoint, params=params, cursor=c)
        all_players = d['data']
        for players in all_players:
            if (players['jersey_number'] is None or players['college'] is None or players['height'] is None or players['weight'] is None or players['country'] is None or players['position'] is None) or (players['jersey_number'] == "" or players['college'] == "" or players['height'] == "" or players['weight'] == "" or players['country'] == "" or players['position'] == ""):
                null_players+=1
                print(f"Player name: {players['first_name']} {players['last_name']}")
                print(f"Player team: {players['team']['full_name']}")
                print(f'Jersey Number: {players['jersey_number']}')
                print(f'College: {players['college']}')
                print(f'Height: {players['height']}')
                print(f'Weight: {players['weight']}')
                print(f'Country: {players['country']}')
                print(f'Position: {players['position']}')
        meta = d['meta']
        c = meta.get('next_cursor')
        print(f"Next_Cursor: {c}")
        page += 1

    print(f"Jogadores com campos nulos: {null_players}")

    #Deram 1313 jogadores com campos nulos