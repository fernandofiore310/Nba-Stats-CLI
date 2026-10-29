import argparse

from sqlite3 import Connection

def execute_query(conn: Connection, args: argparse.Namespace) -> None:

    cursor = conn.cursor()

    if args.data == "wins_and_scoring":

        with open("sql/queries/high_low_scoring_teams_wins.sql", "r", encoding="utf-8") as f:
            script = f.read()

        print("Season | Team | Total Wins | Rank | Total Points Scored")
        cursor.execute(script)

        print(cursor.description) #devolve o nome das colunas e o resto eh None
        print(cursor.fetchall()) #devolve o resultado correto

    elif args.data == "back-to-back":
        pass

    else:
        pass
    