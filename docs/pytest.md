### Como o pytest encontra os testes? Que nomes de arquivo e de função ele procura?
Se nenhum argumento eh especificado no comando de CLI usado, o pytest vai comecar a procurar arquivos test_*.py ou *_test.py no testpaths (se configurado) ou no diretorio em que o comando foi rodado e seus respectivos subdiretorios. Dentro desses arquivos, o pytest vai procurar funcoes ou metodos fora de classes que possuem o prefixo test, metodos dentro de classes com o prefixo Test (sem __init__()).

### Num teste do pytest, você usa o assert comum do Python. O que o pytest mostra quando um assert falha, que o Python puro não mostra?
O pytest mostra um failure report, especificando onde qual resultado nao bate com o valor comparado no assert. O python normal apenas levanta um Assertion error.

### Como rodar um único arquivo de teste? E uma única função de teste?
Para rodar um unico arquivo de teste, eh so passar, ao lado do pytest na linha de comando, o nome do arquivo que voce quer, junto com o diretorio que ele se encontra. Mais especifico, quando queremos rodar apenas uma funcao de um arquivo, voce usa a nomenclatura normal para o arquivo que ja descrevi anteriormente, seguida de :: e o nome da funcao que se quer testar.

### O que o @pytest.mark.parametrize faz? Que erro você cometeu com ele na Fase 0? A resposta está no briefing, em “Expectativa derivada do código”
O parametrize permite que uma funcao seja testada com varios inputs diferentes. Eh um modo mais rapido e pratico para testar possibilidades e casos diferentes para uma mesma funcao. O erro que cometi nele na fase 0 foi que nao sabia que a funcao que queremos testar e seu respectivo assert eram parametros do parametrize, de modo que ficam dentro do seus parenteses de parametros.