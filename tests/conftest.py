from collections.abc import Iterator
from sqlite3 import Connection

import pytest

from nba_stats_cli.db import connect


@pytest.fixture
def conn_memory() -> Iterator[Connection]:
    conn = connect(":memory:") #cria conexao com a base (no caso a nova que vamos usar na RAM) e cria as tabelas
    yield conn
    conn.close()