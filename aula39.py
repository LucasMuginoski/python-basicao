# Introdução a empacotamento e desempacotamento e tuplas

#nome1, nome2, nome3 = ['Maria', 'Helena', 'Luiz']
# print(nome2)

# como pegar apenas 1 valor ou 1 variável?
# *_ é uma variável que não será usada. Equivalente a algo diferente como variavel "*resto"
_ , nome, *_ = ['Maria', 'Helena', 'Luiz']
print(nome)

