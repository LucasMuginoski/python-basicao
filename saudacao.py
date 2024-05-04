"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
entrada = input("Digite a hora em numeros inteiros ")

try:
    hora = int(entrada)
    if hora >= 0 and hora <=11:
        print("Bom dia!")
    elif hora >= 12 and hora <= 17:
        print("Boa tarde!")
    elif hora >= 18 and hora <= 23:
        print("Boa noite!")
    else:
        print("Horário desconhecido")
except:
    print("Por favor digite apenas numeros inteiros.")