fruta = 'manzana'


if fruta == 'kiwi' : #Si y solo si  y las condiciones   <    >     >=      <=      !=      ==
	#print ("el valor es kiwi")
	pass

elif fruta == 'manzana':
	print ("es una manzana")
	#pass #permite condicionar la aplicacion no tiene ninguna salida

elif fruta == 'manzana2':
	print ("es otra manzana")

else :
	print("No son iguales")

#mensaje = 'El valor es kiwi' if fruta == 'kiwi' else 'No son iguales'
#print(mensaje)

#Valores considerados como falso   [], (), {}, 0, '', None

valor = 1 
valor_dos = 20

if valor and valor_dos > 20: #and debe cumplirce las dos condiciones para ser verdaderos
	print('es verdad')
else:
	print('No es verdad')

if valor or valor_dos > 20: #or una de las dos debe cumplir para que sean verdadero
	print('es verdad')
else:
	print('No es verdad')


