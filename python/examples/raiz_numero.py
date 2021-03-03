# Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica. Python3 no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿Cómo se puede calcular?

import math
numero = int(input("Ingrese un numero :"))
cuadrado = math.sqrt(numero)
cubico = numero**(1/3)
print("El valor cuadrado es  :",cuadrado)
print("El valor cubico es  :",cubico)