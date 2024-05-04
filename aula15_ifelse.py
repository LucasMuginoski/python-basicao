# Aula sobre estrutura de repetição if / elif / else
# traduzindo para ... se / se não se / se não

entrada = input('Voce que "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('Você entrou no sistema')
elif entrada == 'sair':
    print('Você saiu do sistema')
else:
    print("Digitou entrada inválida")

# é o equivalente a um aninhamento de if-else em outras linguagens como por exemplo em C que não possui 'elif
# é possivel ter apenas o if, o if-else ou if-elif-else.
