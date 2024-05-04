# Iterando strings com while

#       01234567891011
nome = input("digite seu nome: ")

print(nome)

index = 0
novo_nome = ''

while index < len(nome):
    letra = nome[index]
    novo_nome += f'*{letra}'
    index += 1

print(novo_nome)