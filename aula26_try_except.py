"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

numero = input("Vou dobrar o numero que voce digitou:")

try:
    # condição onde está tudo ok, 'pass'
    # Fail fast => Começa validando já e se errar passa pra exception
    num = float(numero)
    print('float:', num)
    print(f"O dobro de {num} é {num * 2:.2f}")
except:
    print("Isso não é um numero")



# O if checa uma condição e muda o fluxo. Porém não evita erros ou exceção. 
# if numero.isdigit():
#     # É necessário tratar esse valor sempre! Pois input retorna uma string.
#     num = float(numero)
#     print(f"O dobro de {num} é {num * 2:.2f}")
# else:
#     print("Isso não é um numero")


