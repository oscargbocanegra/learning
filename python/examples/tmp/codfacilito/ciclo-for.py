lista = [1,2,3,4,5,6,7,8,9,10]
tupla = (1,2,3,4,5,6,7,8,9,10)

for valor in lista:
	#print(valor)
	pass

#nuevo_rango = range(0,20,2)
for valor in range(0,20,2):
	#print(valor)
	pass

indice = 0
for valor in lista:
	#print(valor, "Tiene el indice ", indice)
	#indice +=1
	pass

for indice, valor in enumerate(lista):
	print(valor, "Tiene el indice", indice)


