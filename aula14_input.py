# Aula sobre input e métodos de entrada de dados

# a variável nome recebe o valor que é solicitado pela função input
nome = input('Qual o seu nome? ')

print(f'o seu nome é {nome}')
# print(f'o seu nome é {nome=}') => Vemos nome da variável = valor da variável
numero_1 = input('Digite um numero: ')
numero_2 = input('Digite outro numero: ')

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

soma = int_numero_1 + int_numero_2
print(f'A soma dos dois numeros é: {soma}')