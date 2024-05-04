"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""
string = "lucas"
outra_variavel = f'{string[:4]}aaass{string[4:]}'
# Não é possívei mudar dados de uma str, int, float ou bool.
# string[4] = 'aaass'
print(string)
print(outra_variavel)

print(string.capitalize())

# Retorna se tem letras maiúsculas True/False
print(string.isupper())