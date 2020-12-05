'''
#Método 1 de calcular a hipotenusa (sem o módulo math)

co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
h = (co ** 2) + (ca ** 2) ** (1/2)
print(f'a hipotenusa equivale a {h:.2f}')
'''

# Método 2 de calcular a hipotenusa (com o módulo math)

import math

co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
h = math.hypot(co, ca)
print(f'a hipotenusa equivale a {h:.2f}')
