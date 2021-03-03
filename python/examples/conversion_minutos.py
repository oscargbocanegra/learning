# Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde. 
# Por ejemplo: 1000 minutos son 16 horas y 40 minutos.

minutos = int(input('Ingrese los minutos a convertir en Horas: '))

horas = minutos // 60
minuto = minutos % 60

print ('El valor de ' + str(minutos) + ' Minutos corresponde a ' + str(horas) + ' Horas con ' +str(minuto)+ ' Minutos')