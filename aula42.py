"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
import decimal


nume_1 = decimal.Decimal('0.1')
nume_2 = decimal.Decimal('0.7')
nume_3 = nume_1 + nume_2
print(nume_3)
print(f'{nume_3:.2f}')

print(round(nume_3, 3))

