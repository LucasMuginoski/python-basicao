# Calculadora com While

while True:
    num1 = input("Digite um numero: ")
    num2 = input("Digite outro numero: ")
    operador = input("Digite o operador (+,-, /, *)")
    
    numeros_validos = None
    num1_float = 0
    num2_float = 0

    try:
        num1_float = float(num1)
        num2_float = float(num2)
        numeros_validos = True
    except Exception as error:
        numeros_validos = None
        print(error)

    if numeros_validos is None:
        print("Um ou ambos os numeros são inválidos! ")
        continue

    operador_permitido = '+-/*'
    if operador not in operador_permitido:
        print('Operador inválido.')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print("Realizando sua conta. Confia o resultado abaixo: ")
    if operador == '+':
        print(f'{num1_float} + {num2_float} = ', num1_float + num2_float)
    elif operador == '-':
        print(f'{num1_float} - {num2_float} = ', num1_float - num2_float)
    elif operador == '/':
        print(f'{num1_float} / {num2_float} = ', num1_float / num2_float)
    elif operador == '*':
        print(f'{num1_float} * {num2_float} = ', num1_float * num2_float)
    else:
        print("Nunca deve chegar aqui!")

    sair = input("Você quer sair? [s]im ").lower().startswith('s')

    if sair is True:
        break
    
