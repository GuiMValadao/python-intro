#----------------------------------
# Aritmetica
#----------------------------------

from math import log10          # Importa log10 do modulo math. Colocar import math requer chamar o modulo math posteriormente usando math.log10
# Qual seria menos exigente computacionalmente:
#   - liberar uma funçao a ser usada livremente no programa (from math import log10)
#   - chamar o modulo e definir a funçao quando for aplicado (import math e no corpo math.log10(a))

# Pede para o usuario colocar dois numeros
a = int(input('insira o valor de a: '))
b = int(input('insira o valor de b: '))

# Realiza e imprime o resultado
print(a, '+', b, '=', a + b)
print(a, '-', b, '=', a - b)
print(a, '*', b, '=', a * b)
print(a, '/', b, '=', a / b)
print(a, '%', b, '=', a % b)
print('O logaritmo na base 10 de', a, 'e', log10(a))
print(a, '^', b, '=', a ** b)
