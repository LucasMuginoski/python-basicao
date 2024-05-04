"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

import os

lista = []
opcao = 0

while opcao != 's':
    print('***** Menu *****')
    opcao = input('[i]nserir [a]pagar [l]istar [s]air:')

    if opcao == 'i':
        #limpa o terminal e add o valor na lista
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
        )
        # try valida se o indice é um inteiro
        try:
            indice = int(indice_str)
            del lista[indice]
        # para cada tipo de erro aparece as msg conforme definido abaixo
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    elif opcao == 's':
        print("Você saiu do programa. ")
    else:
        print('Por favor, escolha i, a, l ou s.')
