# possibilidades de uso da funcao print

print('Como esperado exibe algo na tela', 123) 
print(123, 456, sep="-", end='##')
#diferente de java, o print quebra a linha (lá precisamos usar system.out.println)
print(456, 789, sep='-') 
# notem q após nativamente o interpretador também considerou o espaço e não "juntou" os dois argumentos, o argumento sep definiu um novo separador '-'

# python é case sentive então a funçao print não aceita o P maiúsculo por exemplo