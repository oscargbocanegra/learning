"""
@decorador
def saluda():
	print("Hola Mundo")
	saluda()
"""


def decorador(is_valid = True):
	def _decorador(fun):
		def before_action():
			print("Vamos a ejecutar la funcion")
			def after_action():
				print("Se ejecuto la funcion")
				def nueva_funcion(*args,**kwargs):
					if is_valid:
						before_action()
						resultado = func(*args,**kwargs)
						after_action()
					return resultado
				return nueva_funcion
		return _decorador
@decorador
def suma(num_uno, num_dos):
	return(num_uno + num_dos)
	
	resultado = suma(80,17)
print(80, 17)