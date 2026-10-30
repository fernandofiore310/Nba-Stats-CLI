
from sqlite3 import Connection


def execute_query(conn: Connection, file: str) -> None:

    cursor = conn.cursor()

    if file == "wins_and_scoring":

        with open("sql/queries/high_low_scoring_teams_wins.sql", "r", encoding="utf-8") as f:
            script = f.read()

        # print("Season | Team | Total Wins | Rank | Total Points Scored")
        cursor.execute(script)

        width = 20

        tupla_description = cursor.description #devolve o nome das colunas e o resto eh None
        print(
            f"{tupla_description[0][0]:<{width}} | "
            f"{tupla_description[1][0]:<{width}} | "
            f"{tupla_description[2][0]:<{width}} | "
            f"{tupla_description[3][0]:<{width}} | "
            f"{tupla_description[4][0]:<{width}} | "
            f"{tupla_description[5][0]:<{width}} |"
        )

        res = cursor.fetchall() #devolve o resultado correto
        for team in res:
            print(
                f"{team[0]:<{width}} | "
                f"{team[1]:<{width}} | "
                f"{team[2]:<{width}} | "
                f"{team[3]:<{width}} | "
                f"{team[4]:<{width}} | "
                f"{team[5]:<{width}} |"
            )

    elif file == "back-to-back":
        pass

    else:
        pass
    