# Aula sobre estrutura de repetição While + Break
# Executa uma ação enquanto uma condição for verdadeira
# Operadores de atribuição =, +=, -=,*=, //=, **= e %=  (Todos os aritmeticos podem sem combinados com '=' abribuicao)
# Comendo "continue" retorna ao laço while mais próximo.

contador = 0

while contador < 25:
    contador += 1

    if contador == 6:
        print("Pulei o 6")
        continue

    if contador == 12:
        print("Pulei o 12")
        continue

    if contador == 18:
        print("Pulei o 18")
        continue

    if contador == 24:
        print("Pulei o 24")
        continue

    print(contador)



print("Saimos do lanço")