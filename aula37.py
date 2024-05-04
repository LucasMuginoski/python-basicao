# contatenando listas e estendendo
'''
  extend - estende a lista
    + - concatena listas
'''
lista_a = [1,2,3]
lista_b = [4,5,6]

# faz uma especie de concatenação => gera uma nova lista e joga na lista c
#lista_c = lista_a + lista_b
#print(lista_c)

lista_a.extend(lista_b)
# extend não retorna valoes, logo ele traz none se printar assim ""print(lista_d)""
print(lista_a)