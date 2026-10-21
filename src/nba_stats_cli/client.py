import os
import time
from typing import Any

import requests
from dotenv import load_dotenv


class LimiteTentativasError(Exception):
    pass

MAX_TRIES = 5
TEMPO_BASE = 1

def try_and_retry(endpoint: str, headers: dict[str, Any], params: dict[str, Any], timeout: int, cursor: int | None = None) -> requests.Response:
    
    tentativas = 0
    status : int = 0
    excecoes = (requests.exceptions.Timeout, requests.exceptions.ConnectionError)

    d = params.copy()
    if cursor is not None: d['cursor'] = cursor
    
    while tentativas < MAX_TRIES:
        print(f"Tentativa numero {tentativas+1}")

        backoff: int = TEMPO_BASE * (2**tentativas)

        try:    
            r = requests.get(url=endpoint, headers=headers, params=d, timeout=timeout) #se der erro de timout, essa propria linha vai lancar a excecao
            print(r.url)
        
        except excecoes: #nao se usa or em except, pois nesse caso ele captura apenas a primeira excecao
            # erro de timout nao tem status ou conexao nao tem status. Por isso tratamos eles aqui
            time.sleep(backoff)
            tentativas+=1
            continue
        
        print(f"Status: {r.status_code}, Tipo: {type(r.status_code)}")
        status = r.status_code
    
        if status == 429:
            # print(r.text)
            # print(r.headers)
            # print(r.content)
            sec = r.headers.get('retry-after')
            if sec is not None:
                espera: int = int(sec)
            else:
                espera = backoff
            
            print(f"Tempo a se esperar pos 429: {espera}")
            time.sleep(espera)
            tentativas+=1
        
        elif status >= 500 and status < 600:
            time.sleep(backoff)
            tentativas+=1

        elif status >= 400 and status < 500:
            r.raise_for_status() #essa linha vai lancar a excecao quando a linha de get (ou qualquer outra requisicao) retornou uma resposta, mas com status de erro

        else:
            return r
        
    raise LimiteTentativasError("Numero maximo de tentativas estourado!")

def get_page(endpoint: str, params: dict[str, Any], cursor: int | None = None) -> dict[str, Any]:

    load_dotenv()
    api_key = os.getenv(key="BALLDONTLIE_API_KEY")
    if api_key is None: raise RuntimeError("Chave da API não foi encontrada!")

    headers={"Authorization": api_key}

    url = f"https://api.balldontlie.io/v1/{endpoint}"

    timeout = 5

    r = try_and_retry(endpoint=url, headers=headers, params=params, timeout=timeout, cursor=cursor)
    
    data: dict[str, Any] = r.json()
    return data