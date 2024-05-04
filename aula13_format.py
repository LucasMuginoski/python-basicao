# Função format para formação de strings
a = 'AAA'
b = 'B'
c = 1.1

# string = 'b={1} a ={0} c={2}' => usando indices de posição

string = 'b={nome2} a={nome1} a={nome1} b={nome2} c={nome3:.2f} '

# formato = string.format(a,b,c)
# usando parametros nomeados
formato = string.format(nome1=a,nome2=b,nome3=c)
print(formato)