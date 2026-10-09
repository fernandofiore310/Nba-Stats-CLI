import os
from typing import Any

import requests
from dotenv import load_dotenv


def get_page(endpoint: str, params: dict[str, Any], cursor: int | None = None) -> dict[str, Any]:

    load_dotenv()
    api_key = os.getenv(key="BALLDONTLIE_API_KEY")
    if api_key == None: raise requests.exceptions.HTTPError("Chave da API não foi encontrada!")

    headers={"Authorization": api_key}

    url = f"https://api.balldontlie.io/v1/{endpoint}"
    
    d = params
    if cursor is not None: d['cursor'] = cursor

    timeout = 5

    r = requests.get(url=url, headers=headers, params=d, timeout=timeout) #se der erro de timout, essa propria linha vai lancar a excecao
    r.raise_for_status() #essa linha vai lancar a excecao quando a linha de cima retornou uma resposta, mas com status de erro

    data: dict[str, Any] = r.json()
    return data