# # Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido.

numero = int(input('Digite un numero de dos cifras :'))
decenas = numero // 10
unidades = numero % 10

print (f'El numero ingresado es {numero} El numero invertido es {unidades}{decenas}')

