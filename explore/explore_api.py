import os
import time

import dotenv
import requests

# H1
# Tempo: 25min36s
# Esperado (na mão, antes de rodar): Espero que venham 30 times.
# Conferência: Vieram 89 times.
# Consulta: Pedi para o GPT me ajudar com o uso da chave da API.
# Quando olhei o r.json, vi apenas a chave 'data' do json, cujo valor era uma lista de times

# Esse comando le meu arquivo .env
dotenv.load_dotenv()
#Esse comando procura uma variavel, no arquivo .env, chamada BALLDONTLIE_API_KEY
api_key = os.getenv(key="BALLDONTLIE_API_KEY")

headers={"Authorization": api_key}
timeout = 5
r = requests.get('https://api.balldontlie.io/v1/teams', headers=headers, timeout=timeout)

print(f"Status: {r.status_code}")
r.raise_for_status()

# print(r.headers)
print(f"Tipo de conteudo: {r.headers['content-type']}")

# print(r.content)

teams = r.json()
# print(teams)
list_teams = teams['data']
n_teams = len(list_teams)
print(f"Numero de times: {n_teams}")

# H2
# Tempo: 2min
# Esperado (na mão, antes de rodar): Codigo de status deve ser 401
# Conferência: bateu.
# Consulta: Nenhuma
# (explicação, quando o exercício pedir)

time.sleep(13)

# Esse comando le meu arquivo .env
dotenv.load_dotenv()
#Esse comando procura uma variavel, no arquivo .env, chamada BALLDONTLIE_API_KEY
api_key = os.getenv(key="BALLDONTLIE_API_KEY")

headers={"Authorization": api_key}
timeout = 5
r = requests.get('https://api.balldontlie.io/v1/teams', timeout=timeout)

print(f"Status: {r.status_code}")
# r.raise_for_status()

print(f"Tipo de conteudo: {r.headers['content-type']}")

# H3
# Tempo: 14min11s
# Esperado (na mão, antes de rodar): Codigo de status deve ser 404. O codigo vai quebrar pois estou usando o raise_for_status. Caso nao estivesse usando, ele nao quebraria.
# Conferência: Antes, estava testando com 10000000000000 e estava dando 500. Supus que o servidor nao esperava um numero tao grande, entao troquei por 645, e veio o 404 esperado. Alem disso, testei com o raise_for_status comentado e realmente nao quebra o codigo (o codigo quebrou na parte que tento extrair os dados do r.json, visto que nao voltou json algum).
# Consulta: Nenhuma
# (explicação, quando o exercício pedir)

time.sleep(13)

# Esse comando le meu arquivo .env
dotenv.load_dotenv()
#Esse comando procura uma variavel, no arquivo .env, chamada BALLDONTLIE_API_KEY
api_key = os.getenv(key="BALLDONTLIE_API_KEY")

headers={"Authorization": api_key}
# params = {'ID': 10000000000000}
ID = 645 #ID de times para filtrar resultado eh path parameter, e nao query parameter
timeout = 5
r = requests.get(f'https://api.balldontlie.io/v1/teams/{ID}', headers=headers, timeout=timeout)

print(r.url)

print(f"Status: {r.status_code}")
# r.raise_for_status()

# print(r.headers)
print(f"Tipo de conteudo: {r.headers['content-type']}")

# print(r.content)

# teams = r.json()
# print(teams)
# list_teams = teams['data']
# n_teams = len(list_teams)
# print(f"Numero de times: {n_teams}")

# H4
# Tempo: 6min40s
# Esperado (na mão, antes de rodar): Espero que o codigo crashe, sem nem retornar status, visto que nao foi nem possivel completar a requisicao.
# Conferência: Eu esperava um TimeoutError. Usei o try/except para evitar que o codgio crashasse, no entanto ele crashou com um ConnectTimoutError.
# Consulta: Nenhuma
# (explicação, quando o exercício pedir)

time.sleep(13)

# Esse comando le meu arquivo .env
dotenv.load_dotenv()
#Esse comando procura uma variavel, no arquivo .env, chamada BALLDONTLIE_API_KEY
api_key = os.getenv(key="BALLDONTLIE_API_KEY")

headers={"Authorization": api_key}
timeout = 0.001

try:
    r = requests.get('https://api.balldontlie.io/v1/teams', headers=headers, timeout=timeout)
except requests.exceptions.Timeout as e:
    print(e)

# H5
# Tempo: 8min40s
# Esperado (na mão, antes de rodar): 
# Conferência: 
# Consulta: Nenhuma
# Algo estranho que percebi. Em relacao ao draft, realmente vem valores nulos (testei com o Austin Reaves).
# Em seguida, sabia que Nikola Jokic e Doncic nao tinham feito college no estados unidos. No entanto, no caso deles, o college aparece como o clube que jogaram antes de vir para a NBA. Alem disso, o country eh a nacionalidade do jogador, considerando que para Luka aparecia o college como Real Madrid e country como Slovenia.
# Mas mais interessante que isso foi o caso Luka Doncic. Apareceram 3 Lukas diferentes quando eu puxei os dados. O Luka atual, jogador do Lakers, com todos os dados preenchidos. No entanto, apareceram outros dois, Lukas que estavam como jogadores do Real madrid. Nesses casos, as colunas height, weight, jersey_number, college, country, as do draft estavam nulas.
# Alem disso, nesse mesmo caso do Luka, o Real Madrid aparecia com as seguintes colunas com valores nulos: conferencia, divisao. E a cidade vinha como Real Madrid, deixando o full_name do time como Real Madrid Real Madrid.
# Por fim, testei com jogadores que ja se aposentaram, como Charles Barkley, e eles aparecem com o jersey number que usavam no time que esta associado a ele. So que diferente de Luka, so aparecia um Charles Barkley, associado ao 76ers, mesmo tendo jogado em outros clubes

time.sleep(13)

# Esse comando le meu arquivo .env
dotenv.load_dotenv()
#Esse comando procura uma variavel, no arquivo .env, chamada BALLDONTLIE_API_KEY
api_key = os.getenv(key="BALLDONTLIE_API_KEY")

headers={"Authorization": api_key}
params = {'first_name': 'Charles', 'last_name': 'Barkley'}
timeout = 5

r = requests.get('https://api.balldontlie.io/v1/players', headers=headers, params=params, timeout=timeout)

players = r.json()['data']
print(players)

# H6
# Tempo: 9min19s
# Esperado (na mão, antes de rodar): Para pedir a segunda pagina, imagino que seja com 'cursor': 2 no params.
# Conferência: Entendi. O curso eh como se fosse um ponteiro. Logo, se o cursor for igual a 0 ele vai apontar para o primeiro jogador da base. Ai o tamanho das paginas a gente mesmo define. Como estou usando 5 como per_page, a primeira pagina seria cursor=0 e a segunda cursor=5.
# Consulta: Nenhuma
# (explicação, quando o exercício pedir)

time.sleep(13)

# Esse comando le meu arquivo .env
dotenv.load_dotenv()
#Esse comando procura uma variavel, no arquivo .env, chamada BALLDONTLIE_API_KEY
api_key = os.getenv(key="BALLDONTLIE_API_KEY")

headers={"Authorization": api_key}
params = {'cursor': 5, 'per_page': 5}
timeout = 5

r = requests.get('https://api.balldontlie.io/v1/players', headers=headers, params=params, timeout=timeout)

players = r.json()
print(players)