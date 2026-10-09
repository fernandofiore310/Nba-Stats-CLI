import time
from typing import Any

from nba_stats_cli.cliente import get_page

if __name__ == "__main__":
    endpoint = "players"
    params: dict[str, Any] = {}
    c1 = 0
    dic = get_page(endpoint=endpoint, params=params, cursor=c1)
    print(dic['data'])