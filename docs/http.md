### O que compõe uma requisição e uma resposta HTTP?
Uma requisição em HTTP é composta pela linha principal, que vai ter o metodo http, a url, os endpoint e possivelmente os query parameters; pelo HEADER, que adicionam contexto ao pedido, por exemplo, passar a chave autenticadora da API ou passar o formato que voce quer que a respota venha; e o Body, que vai conter informacoes que o servidor precisa, por exemplo, quando um usuario esta se cadastrando pela primeira vez em um site, e precisa criar usuario e senha, nesse caso, ele manda as infos para o servidor.
Ja uma resposta http é composta pelo STATUS, que vai dizer o que aconteceu com aquela requisicao que o cliente fez; o HEADER, que vai conter a resposta de infos pedidas pelo cliente no seu proprio header; e o BODY, que vai conter os dados que o cliente requisitou.

### O que significam os códigos 401, 404 e 429? Qual deles faz sentido tentar de novo, e por quê?
401: é necessário autenticação. Provavelmente o cliente não possui uma chave válida e por isso não tem acesso aos dados.
404: recurso não encontrado. Talvez algum parâmetro ou algo da linha principal foi passado errado por parte do cliente, como um id que não existe no banco de dados.
429: requisições demais, quando o cliente ultrapassa o seu limite de requisições.

O único que faz sentido tentar de novo é o 404 (após mudança do parâmetro claro), visto que no 401 o cliente não tem autorização, logo não vai conseguir de jeito nenhum, e no 429 o cliente tem que esperar as suas requisições reiniciarem.

### Quando o servidor responde 404, o requests lança uma exceção sozinho? O que você precisa fazer para que ele lance?
Não, ele segue normal. Para que o programa seja interrompido e o desenvolvedor consiga ver onde o erro está, devemos usar o .raise_for_status() que basicamente raise exceptions em casos de bad requests (4xx e 5xx).

### Por que toda requisição deveria ter um timeout?
Porque caso ele nao seja usado, uma requisicao pode ficar rodando por tempo indefinido, o que seria ruim para o cliente.