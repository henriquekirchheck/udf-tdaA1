# Projeto A1 UDF Tecnica de Desenvolvimento de Algoritimo

| Conteudo                        | Arquivo                          | Comando para executar        |
| ------------------------------- | -------------------------------- | ---------------------------- |
| Estruturas Condicionais         | conditionals/\_\_main\_\_.py     | `python -m conditionals`     |
| Estruturas de Repetição (while) | repetition/while/\_\_main\_\_.py | `python -m repetition.while` |
| Estruturas de Repetição (for)   | repetition/for/\_\_main\_\_.py   | `python -m repetition.for`   |
| Listas                          | lists/\_\_main\_\_.py            | `python -m lists`            |
| Dicionarios                     | dicts/\_\_main\_\_.py            | `python -m dicts`            |

## Estruturas Condicionais

Um sistema de verificação de idade para eventos. Digite a idade e receba uma resposta indicando se é permitida a entrada.

```
> python -m conditionals
Digite a idade da pessoa: 17
Rejeitado
> python -m conditionals
Digite a idade da pessoa: 19
Aprovado
```

## Estruturas de Repetição

Um contador de numeros pares de 1 até 100, execute e veja a contagem.

```
> python -m repetition
2
4
6
8
10
12
14
16
18
20
...
```

## Listas

Um banco de dados de nomes, digite nomes para guardar eles numa lista e não digite nada para sair do programa e mostrar os nomes indicados.

```
> python -m lists
Digite um nome para adicionar a lista (exit para sair): Henrique
Digite um nome para adicionar a lista (exit para sair): João
Digite um nome para adicionar a lista (exit para sair): Flavio
Digite um nome para adicionar a lista (exit para sair): exit

Henrique
João
Flavio
```

## Dicionarios

Um banco de dados de produtos, cadastre produtos indicando o nome e o preço do produto e saia do programa com o comando exit.

```
> python -m lists
Digite um produto para adicionar ao dicionario (formato: "{nome} R${preço}") (exit para sair): Computador R$1000.45
Digite um produto para adicionar ao dicionario (formato: "{nome} R${preço}") (exit para sair): Maquina de lavar R$1000.46
Digite um produto para adicionar ao dicionario (formato: "{nome} R${preço}") (exit para sair): Bola R$1001.43
Digite um produto para adicionar ao dicionario (formato: "{nome} R${preço}") (exit para sair): Ouro R$2.76
Digite um produto para adicionar ao dicionario (formato: "{nome} R${preço}") (exit para sair): exit

Produto
Nome: Computador
Preço: R$1000.45

Produto
Nome: Maquina de lavar
Preço: R$1000.46

Produto
Nome: Bola
Preço: R$1001.43

Produto
Nome: Ouro
Preço: R$2.76

```
