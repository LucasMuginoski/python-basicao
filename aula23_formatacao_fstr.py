# Método mais moderno se comparado com interpolação

"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}') # var > preenche a esquerda com espaços até dar 10 caracteres
print(f'{variavel: <10}.') # var < preenche a direita com espaços até dar 10 caracteres
print(f'{variavel: ^10}.') # var ^ com espaços e mantém a string centralizada (espaços string espaços), pode add outros valores se colocar antes do ^
print(f'{1000.4873648123746:0=+10,.1f}') # 
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')