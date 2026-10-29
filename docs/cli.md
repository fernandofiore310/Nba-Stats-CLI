### O que é um argumento posicional e o que é um opcional? Como cada um aparece quando o usuário digita o comando? Dê um exemplo de cada.
Um argumento posicional eh um argumento que meu programa espera e que tem uma posicao especifica. Ja o opcional eh um argumento sem posicao especifica que meu programa pode receber, mas nao espera/precisa dele necessariamente.
Argumentos opcionais aparecem com - ou --, ja posicionais aparecem so com o valor. Entao imagine que eu quero pegar um jogador especifico. Tenho first_name e last_name como argumentos posicionais, enquanto tenho time como opcional. Nesse caso, chamaria o programa como:
python3 main.py Luka Doncic --team Lakers (caso nao estivesse usando um default por exemplo).

### Depois que o argparse lê o que foi digitado, como o programa acessa os valores?
Assim que o argparse le os valores, ele cria um objeto Namespace, no qual eh possivel acessar os valores e os argumentos. Entao, quando usamos:
(considere que parser = argparse.ArgumentParser())
args = parser.parse_args()
podemos acessar os argumentos fazendo (caso ja tivemos criado o parser.add.argument()):
args.first_name
Luka

### O que são subcomandos (subparsers)? Use o git como exemplo: git commit e git push são o mesmo programa, com subcomandos diferentes. Como o programa sabe qual subcomando foi digitado?
Subparsers eh uma operacao especifica dentro de um programa de CLI. Ele permite que se crie operacoes com seus proprios argumentos, como se cada subparser tivesse o seu parser. Por exemplo, o git commit e o git push sao o mesmo programa, no entanto, commit e push sao subparsers diferentes, cada um com seus argumentos (posicionais ou obrigatorios) e cada um com uma funcao de execucao. 
O progrma sabe identificar qual programa foi digitado quando se usa o add_subparser() e usando o argumento dest dele para salvar o comando no Parser principal, e depois, usar o subparser.add_parser() para definir o nome do subparser (que vai ser salvo em args.command caso dest="command") e vai identificar a operacao.

### O que o argparse gera sozinho quando o usuário digita --help?
Ele gera uma resposta de "ajuda" na teoria, porem nao diz muito. Eh o unico argumento (opcional no caso) que ja vem com o argparse.

### Desenho
Antes de tudo, o Parser principal nao vai ter argumentos posicionais. Acredito que o usuario so vai querer rodar o arquivo com as funcoes (subcomandos/subparsers). Logo, nao serao necessarios argumentos posicionais no Parser principal. Ele vai ter alguns argumentos opcionais, como o --help e o --verbose por exemplo. Acredito que esses possam ajudar o usuario durante o uso do programa.
Agora, os subparsers terao argumentos posicionais e opcionais.

- load
Ele sera o comando responsavel pela extracao dos dados, desde o contato com a API, ate os dados manipulados/transformados no banco de dados.
Ele tera um argumento posicional, que podera ter tres valores: teams, players e games (posso usar o checks para isso se nao me engano, e sem default pois caso o usuario nao especifique o programa deve travar e nao carregar algo que nao foi pedido). Alem disso, ele tera um argumento opcional para temporadas, que so fara sentido para o load games. Na versao atual do projeto, so faz sentido pegar as temporadas 2024 e 2025. O valor default (caso o usuario digite apenas --seasons sera as temporadas 2024 e 2025). Quem sabe em versoes maois avancadas isso melhore. 
Exemplos de uso:
load teams
> Loading teams...
> Teams loaded in database

load players
> Loading players...
> Players loaded in database

load games
> ERROR (mensagem de erro que posso definir)

load games
> Loading games from [seasons] season(s)
> Games loaded in database

- query
Esse subparser vai ser responsavel por rodar as tres queries que defini (vitorias, back-to-back e colleges) e outras possiveis que eu queira adicionar em outras versoes do projeto.
Nesse caso, ela vai precisar ter um argumento posicional, que vou definir um nome curto (noa vai ser o nomme do arquivo .sql) quando as queries estiverem prontas, que vai especificar exatamente qual query devera ser rodada (que se encontram na pasta sql/queries/) e exibida no terminal.
Exemplos de uso:

query wins_points
> [query formatada de maneira bonita]

query
> ERROR (mensagem de erro que posso definir)