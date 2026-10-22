import pytest
from nba_stats_cli.db import connect, create_cursor, record_teams

from sqlite3 import Connection
from typing import Iterator

@pytest.fixture
def conn_memory() -> Iterator[Connection]:
    conn = connect(":memory:") #cria conexao com a base (no caso a nova que vamos usar na RAM) e cria as tabelas
    yield conn
    conn.close()