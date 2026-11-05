from collections.abc import Iterator
from sqlite3 import Connection

import pytest

from nba_stats_cli.db import connect


@pytest.fixture
def conn_memory() -> Iterator[Connection]:
    conn = connect(":memory:") #cria conexao com a base (no caso a nova que vamos usar na RAM) e cria as tabelas
    yield conn
    conn.close()

@pytest.fixture
def teams_list() -> list[tuple[int, str, str, str, str, str, str]]:
    teams_list = [(2, 'East', 'Atlantic', 'Boston', 'Celtics', 'Boston Celtics', 'BOS'), (4, 'East', 'Southeast', 'Charlotte', 'Hornets', 'Charlotte Hornets', 'CHA'), (6, 'East', 'Southeast', 'Cleveland', 'Cavaliers', 'Cleveland Cavaliers', 'CLE')]
    return teams_list