"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input('Digite um numero inteiro: ')
num_inteiro = int(numero)

par = num_inteiro % 2
if par == 0:
    print(f"O numero {num_inteiro} é par")
else:
    print(f"O numero {num_inteiro} é ímpar")