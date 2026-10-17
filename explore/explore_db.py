from nba_stats_cli.cliente import get_page
from nba_stats_cli.db import connect, record_teams, close_connection
from nba_stats_cli.transform import team_params

if __name__ == "__main__":
    endpoint = "teams"
    params = {}
    c = 0
    d = get_page(endpoint=endpoint, params=params, cursor=c)

    all_teams = d['data']
    nba_teams = [team for team in all_teams if team['id'] > 0 and team['id'] <= 30]
    assert len(nba_teams) == 30
    nba_teams_tuple_list = []

    for t in nba_teams:
        nba_teams_tuple_list.append(team_params(t))
    
    conn = connect()
    record_teams(conn, nba_teams_tuple_list)
    close_connection(conn=conn)