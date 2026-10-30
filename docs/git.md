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

