def generador(*args):
	""" Recibe N cantidad de numeros  en este espacio se escribe que hace la funcion"""
	for valor in args:
		yield valor * 10, True
	return valor * 10
for valor in generador(1,2,3,4,5,6,7,8,9,10):
	print(valor)

	documentacion = generador.__doc__
	print(documentacion)