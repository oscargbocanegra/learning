def crearfuncion(num_uno, num_dos): #closure
	def validacion():
		print('Se esta ejecutando validación')
		return num_uno > 0 and num_dos > 0
	return validacion

def aplicar_funcion(func):
	resultado = func() # v o f
	print(resultado)

nueva_funcion = crearfuncion(10,9)
aplicar_funcion(nueva_funcion)