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
Fiquei sem tempo para implementar