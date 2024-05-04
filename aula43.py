"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""
frase = '  Olha só que  ,    coisa interessante!'
lista_palavras = frase.split() # sem argumento ele vai dividir nos espaços em brancos
# print(lista_palavras)


lista_frases_cruas = frase.split(',')
lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    #strip é usado para retirar os espaços na string
    lista_frases.append(lista_frases_cruas[i].strip())

print(lista_frases_cruas)
print(lista_frases)

frases_unidas = ','.join(lista_frases)
print(frases_unidas)