contador = 0
bandera = True

while bandera:
	print(contador)
	contador +=1 # contador = contador + 1

	if contador == 5: 
		#print('Estamos en el numero 5')
		continue

	if contador == 6: 
		#print('Estamos en el numero 5')
		bandera = False # break

else: 
	print('El while ha terminado')

