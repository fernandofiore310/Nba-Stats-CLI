import os
from typing import Any

import requests
from dotenv import load_dotenv


def busca_pagina(endpoint: str, params: dict[str, Any], cursor: int | None = 0) -> dict[str, Any]:
    load_dotenv()

    try:
        api_key = os.getenv(key="BALLDONTLIE_API_KEY")

    except requests.exceptions.HTTPError:
        print("Chave da API não foi encontrada!")

    headers={"Authorization": api_key}
    timeout = 5
    if cursor != 0: params['cursor'] = cursor

    try:
        r = requests.get(endpoint, headers=headers, params=params, timeout=timeout)

    except requests.exceptions.Timeout:
        print("TIMEOUT!!!")

    return r.json()