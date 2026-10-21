### O que é tipagem nominal e o que é tipagem estrutural? Em qual delas o Protocol se encaixa?
Tipagem nominal eh quando a tipagem eh feita/aceita baseada em heranca. Entao, uma objeto eh de um tipo especifico porque herda dessa classe pai.
Tipagem estrutural eh quando a tipagem eh feita/aceita baseada se a classe tem a mesma estrutura de outra. Ou seja, um objeto pode ser considerado de um tipo especifico, caso ele tenha a mesma estrutura que outro (mesmos metodos e atributos).

### Para um objeto ser aceito onde se espera um Protocol, ele precisa herdar dele?
Nao, ele apenas precisa ter a mesma estrutura, no caso, os mesmos metodos e atributos da classe com Protocol.

### Quem confere se um objeto cumpre o Protocol: o Python, quando o programa roda, ou o mypy?
O mypy, visto que sem o Protocol, o checador espera apenas a tipagem nomminal, e da erro caso o desenvolvedor use tipagem estrutural sem Protocol.

### No seu projeto, o que um Protocol de cliente da API precisaria ter? Escreva só a lista: o nome do método, os parâmetros e o retorno.
O cliente precisaria ter o metodo try_and_retry, alem dos parametros padrao de uso da API, como o endpoint, o header, os params, e o timeout. Alem disso, o metodo precisa retornar a resposta (requests.Response).