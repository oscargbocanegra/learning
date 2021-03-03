# Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. 
# Recordar que la fórmula para la conversión es: C= (F-32)*5/9

grados_f = int(input('Ingrese el valor de grados Fahrenheit a convertir: '))

celcius = (grados_f-32)*5/9

print ('Los grados Celius son ' + str(celcius))
