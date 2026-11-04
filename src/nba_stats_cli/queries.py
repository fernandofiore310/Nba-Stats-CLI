
from sqlite3 import Connection


def execute_query(conn: Connection, script: str) -> None:

    columns = []

    cursor = conn.cursor()

    cursor.execute(script)

    tupla_description = cursor.description #devolve o nome das colunas e o resto eh None
    for tupla in tupla_description:
        columns.append(tupla[0])

    lines = cursor.fetchall() #devolve o resultado correto

    return columns, lines

    # print(
    #     f"{tupla_description[0][0]:<{width}} | "
    #     f"{tupla_description[1][0]:<{width}} | "
    #     f"{tupla_description[2][0]:<{width}} | "
    #     f"{tupla_description[3][0]:<{width}} | "
    #     f"{tupla_description[4][0]:<{width}} | "
    #     f"{tupla_description[5][0]:<{width}} |"
    # )

    # for team in res:
        # print(
        #     f"{team[0]:<{width}} | "
        #     f"{team[1]:<{width}} | "
        #     f"{team[2]:<{width}} | "
        #     f"{team[3]:<{width}} | "
        #     f"{team[4]:<{width}} | "
        #     f"{team[5]:<{width}} |"
        # )