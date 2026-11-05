from sqlite3 import Connection
from typing import Any


def execute_query(conn: Connection, script: str) -> tuple[list[str], list[tuple[Any, ...]]]:

    columns = []

    cursor = conn.cursor()

    cursor.execute(script)

    tupla_description = cursor.description #devolve o nome das colunas e o resto eh None
    for tupla in tupla_description:
        columns.append(tupla[0])

    lines = cursor.fetchall() #devolve o resultado correto

    return columns, lines