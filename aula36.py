"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista = [1, 2, 3, 4]
#     i =0, 1, 2, 3
print(lista)
num = lista[2]
print(num)
lista[2] = 30
print(lista)
del lista[3]
print(lista)
# adicionar ao final
lista.append(5)
lista.append('bb')
print(lista)
#remove o ultimo elemento da lista
ultimo_removido = lista.pop() 
print(lista, "removido", ultimo_removido)

#lista.clear()
# insert recebe 2 argumentos, primeiro o indice e o segundo é o valor
# estou inserindo o valor 5 no indice 0 (começo da lista)
lista.insert(0, 5)
print(lista)
