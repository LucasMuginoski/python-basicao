"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input("Digite seu primeiro nome ")
comprimento = len(nome)


if comprimento > 1:
    if comprimento < 5:
        print("Seu nome é curto.")
    elif comprimento < 7:
        print("Seu nome é normal.")
    elif comprimento >= 7:
        print("Seu nome é muito grande.")
else:
    print('Digite mais de uma letra.')