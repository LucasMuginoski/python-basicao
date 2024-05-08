# Gerador de numeros de cpf válidos
import random


print("Lista de 50 possíveis números de CPF: ")
for _ in range(50):
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0,9))

    contador_regressivo_1 = 10
    somatorio_digito_1 = 0
    for digito in nove_digitos:
        somatorio_digito_1 += int(digito) * contador_regressivo_1
        contador_regressivo_1 -=1

    digito_1 = (somatorio_digito_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    dez_digitos = nove_digitos + str(digito_1)

    contador_regressivo_2 = 11

    somatorio_digito_2 = 0
    for digito in dez_digitos:
        somatorio_digito_2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1

    digito_2 = (somatorio_digito_2 * 10) % 11

    digito_2 = digito_2 if digito_2 <= 9 else 0

    # digito 1 e digito 2 são os digitos verificadores
    cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'
    print(cpf_gerado_pelo_calculo)