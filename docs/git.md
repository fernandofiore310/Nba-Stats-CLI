## Perguntas

### Qual a diferença entre a main local e a origin/main?
A main local eh a branch no meu computador. Posso atualizar e mexer em arquivos nela normalmente A origin/main eh uma especie de tracker da branch main remota. Basicamente ele marca onde a branch remota estava na ultima vez que eu interagi com o repositorio remoto.

### O que o git fetch faz, e em que ele é diferente do git pull?
O fetch apenas atualiza o tracker da branch, sem mexer na branch local. Ao passo que o git pull, nao so atualiza o tracker como incorpora as mudancas na branch local (um fetch seguido de um merge).

### O que o rebase faz com os commits da sua branch? Desenhe com letras (A, B, C...), antes e depois.
O rebase pega commits que foram feitos em uma branch, separados da main ou de qualquer outra branch por exemplo e apenas cria copias desses commits e os adiciona depois do ultimo commit da main ou outra branch. Ele lineariza o historico de commits do projeto.
Antes:
A --- B --- E --- F
      \
       C --- D
Depois:
A --- B --- E --- F --- C' --- D'
Vale lembrar que eh sempre bom dar um fetch antes do rebase, para ficar atualizado com o estado atual da branch que queremos fazer o rebase em cima.

### Por que, depois de um rebase numa branch que já está no GitHub, o push comum é recusado? O que o --force-with-lease faz de diferente do --force?

## Exercicio pratico
### Passo 1, 2, 3
Estado na branch CLI_feature pre fetch:

(.venv) ffiore310@XPS14310:~/dev/Nba-Stats-CLI$ git log --oneline --graph --all
* b350ac9 (HEAD -> CLI_feature) Atualizacao forcada do README.md na branch
* 82bc32a (origin/CLI_feature) Esqueci de mandar essa parte que nao tinha salvo
* f5cc6ae Leitura do git feita e perguntas respondidas, tirando a ultima que nao deu tempo
* c3b81dc Parte da linha de comando feita. No entanto, falta implementar o corpo para as outras queries no queries.py e nao consegui fazer o test das queries. Nao entendi muito bem como vou testar artificialmente, alem do tempo ter estourado.
* 1453547 Tempo esgotado. Consegui fazer praticamente tudo. Argparse esta praticamente pronto. Unica coisa que falta eh na funcao de executar as queries, onde preciso formatar certinho a exibicao dos resultados e fazer as outras queries e suas respectivas extracoes. Atualizei o pyproject.toml e rodei o pip intall -e . Esta funcional
* 1b4f5ba Desenho dos comandos CLI feitos
* 325f54a Branch criada
| * e2dddf2 (origin/main, origin/HEAD, main) Atualizando upsert da tabela nova e arrumando erros pequenos
|/  
* 6864991 Leitura teorica feita

### Passo 4
Estado na branch CLI_feature pos fetch:

(.venv) ffiore310@XPS14310:~/dev/Nba-Stats-CLI$ git fetch origin
Enter passphrase for key '/home/ffiore310/.ssh/id_ed25519': 
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (3/3), 1.02 KiB | 348.00 KiB/s, done.
From github.com:fernandofiore310/Nba-Stats-CLI
   e2dddf2..3a1b27f  main       -> origin/main

(.venv) ffiore310@XPS14310:~/dev/Nba-Stats-CLI$ git log --oneline --graph --all
* b350ac9 (HEAD -> CLI_feature) Atualizacao forcada do README.md na branch
* 82bc32a (origin/CLI_feature) Esqueci de mandar essa parte que nao tinha salvo
* f5cc6ae Leitura do git feita e perguntas respondidas, tirando a ultima que nao deu tempo
* c3b81dc Parte da linha de comando feita. No entanto, falta implementar o corpo para as outras queries no queries.py e nao consegui fazer o test das queries. Nao entendi muito bem como vou testar artificialmente, alem do tempo ter estourado.
* 1453547 Tempo esgotado. Consegui fazer praticamente tudo. Argparse esta praticamente pronto. Unica coisa que falta eh na funcao de executar as queries, onde preciso formatar certinho a exibicao dos resultados e fazer as outras queries e suas respectivas extracoes. Atualizei o pyproject.toml e rodei o pip intall -e . Esta funcional
* 1b4f5ba Desenho dos comandos CLI feitos
* 325f54a Branch criada
| * 3a1b27f (origin/main, origin/HEAD) Atualizacao forcada de README.md na main
| * e2dddf2 (main) Atualizando upsert da tabela nova e arrumando erros pequenos
|/  
* 6864991 Leitura teorica feita

Ponto importante: esqueci de colocar o que eu esperava ver em cada um desses passos que acabei de fazer. Vou fazer isso nos proximos.

### Passo 5
Antes: O rebase deve dar conflito, visto que os readmes das branches estao diferentes, entao devo arrumar o readme manualmente, ate que nenhuma alteracao da branch sobrescreva a ultima versao da main (apontada por origin/main).


