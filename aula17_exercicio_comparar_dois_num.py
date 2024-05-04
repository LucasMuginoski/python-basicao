# Compare 2 numeros e veja qual é o maior

primeiro_valor = input("Digite um numero inteiro: ")
segundo_valor = input("Digite outro numero inteiro: ")

primeiro_int = int(primeiro_valor)
segundo_int = int(segundo_valor)

if primeiro_int > segundo_int:
    print(f'primeiro valor "{primeiro_int}" é maior que o segundo valor "{segundo_int}"')
elif segundo_int > primeiro_int:
    print(f'segundo valor "{segundo_int}" é maior que o primeiro valor "{primeiro_int}"')
else:
    print('Os valores são iguais entre si')
