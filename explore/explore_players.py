from nba_stats_cli.cliente import get_page

if __name__ == "__main__":
    endpoint = "players"
    team_ids = list(range(1, 31))
    params = {'per_page': 100, 'team_ids[]': team_ids}
    c = 0
    page = 0
    null_players = 0
    null_players_dic = {'jersey_number': 0, 'college': 0, 'height': 0, 'weight': 0, 'country': 0, 'position': 0}

    while c is not None:
        d = get_page(endpoint=endpoint, params=params, cursor=c)
        all_players = d['data']
        for players in all_players:
            if (players['jersey_number'] is None or players['college'] is None or players['height'] is None or players['weight'] is None or players['country'] is None or players['position'] is None) or (players['jersey_number'] == "" or players['college'] == "" or players['height'] == "" or players['weight'] == "" or players['country'] == "" or players['position'] == ""):
                null_players+=1
                
            if players['jersey_number'] is None or players['jersey_number'] == "":
                null_players_dic['jersey_number'] += 1

            if players['college'] is None or players['college'] == "":
                null_players_dic['college'] += 1

            if players['height'] is None or players['height'] == "":
                null_players_dic['height'] += 1

            if players['weight'] is None or players['weight'] == "":
                null_players_dic['weight'] += 1

            if players['country'] is None or players['country'] == "":
                null_players_dic['country'] += 1

            if players['position'] is None or players['position'] == "":
                null_players_dic['position'] += 1

        meta = d['meta']
        c = meta.get('next_cursor')
        print(f"Next_Cursor: {c}")
        page += 1

    print(f"Jogadores com campos nulos: {null_players}")
    print("Frequencia de campos nulos:")
    print(null_players_dic)

    # Resultados no terminal
    # Jogadores com campos nulos: 1314
    # Frequencia de campos nulos:
    # {'jersey_number': 1290, 'college': 1048, 'height': 1104, 'weight': 1112, 'country': 1096, 'position': 597}