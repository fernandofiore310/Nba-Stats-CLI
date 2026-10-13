import time
from typing import Any

import requests

from nba_stats_cli.cliente import get_page

if __name__ == "__main__":
    endpoint = "players"
    params: dict[str, Any] = {}
    c = 0
    dic = get_page(endpoint=endpoint, params=params, cursor=c)
    print(dic)

    #R2
    endpoint = "teams/645"
    params = {}
    c2 = 0
    try:
        dic2 = get_page(endpoint=endpoint, params=params, cursor=c2)
        print("Erro: Excecao deveria ter sido lancada!")
    except requests.exceptions.HTTPError as e:
        print(e.response)

    print("Espera 1 minuto")
    time.sleep(60)

    #R1
    # Antes: Ele vem na sexta chamada e o Retry-After pede 60 segundos de espera.
    # Confere: Bateu
    # O 429 veio na sexta chamada como o esperado, esperou 60 segundos, e foi na segunda tentativa.
    endpoint = "teams/21"
    params = {}
    c3 = 0
    i = 0
    while i < 7:
        print(f"Chamada {i+1}")
        dic3 = get_page(endpoint=endpoint, params=params, cursor=c3)
        i+=1
    print(dic3)