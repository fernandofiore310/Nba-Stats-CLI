import os
from typing import Any

import requests
from dotenv import load_dotenv

import time

MAX_TRIES = 5
TEMPO_BASE = 1

def try_and_retry(endpoint: str, headers: dict[str, Any], params: dict[str, Any], timeout: int, cursor: int | None = None) -> dict[str, Any]:
    
    tentativas = 0
    
    while tentativas < MAX_TRIES:
        print(f"Tentativa numero {tentativas+1}")

        backoff: int = TEMPO_BASE * (2**tentativas)

        try:    
            r = requests.get(url=endpoint, headers=headers, params=params, timeout=timeout) #se der erro de timout, essa propria linha vai lancar a excecao
        
        except requests.exceptions.ConnectTimeoutError or requests.exceptions.ConnectionError:
            time.sleep(backoff)
            tentativas+=1
            continue
        
        print(f"Status: {r.status_code}, Tipo: {type(r.status_code)}")
        status : int = r.status_code
    
        if status == 429:
            # print(r.text)
            # print(r.headers)
            # print(r.content)
            print(f"Tempo a se esperar pos 429: {int(r.headers['retry-after'])}")
            espera = int(r.headers['retry-after'])
            time.sleep(espera)
            tentativas+=1
        
        elif status >= 500 and status < 600:
            time.sleep(backoff)
            tentativas+=1

        elif status >= 400 and status < 500:
            r.raise_for_status() #essa linha vai lancar a excecao quando a linha de get (ou qualquer outra requisicao) retornou uma resposta, mas com status de erro

        else:
            break
        
    return r

def get_page(endpoint: str, params: dict[str, Any], cursor: int | None = None) -> dict[str, Any]:

    load_dotenv()
    api_key = os.getenv(key="BALLDONTLIE_API_KEY")
    if api_key == None: raise requests.exceptions.HTTPError("Chave da API não foi encontrada!")

    headers={"Authorization": api_key}

    url = f"https://api.balldontlie.io/v1/{endpoint}"
    
    d = params
    if cursor is not None: d['cursor'] = cursor

    timeout = 5

    r = try_and_retry(endpoint=url, headers=headers, params=d, timeout=timeout, cursor=cursor)
    
    data: dict[str, Any] = r.json()
    return data