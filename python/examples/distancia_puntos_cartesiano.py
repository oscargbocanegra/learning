#Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano. Calcula y muestra la distancia entre ellos.

import math
print("Ingrese coordenadas punto 1:")
x1 = int(input('Valor X1: '))
y1 = int(input('Valor Y1: '))
print("Ingrese coordenadas punto 2:")
x2 = int(input('Valor X2: '))
y2 = int(input('Valor Y2: '))
distancia = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
print("La distancia es :",distancia)