"""def factorial
_numero():
	numero = 5
	factorial = 1
	while numero > 0:
		factorial = factorial * numero
		numero -=1
		print(factorial)

factorial_numero()
"""
"""
#Funciones con paso de argumentos
def factorial_numero(numero):
	factorial = 1
	while numero > 0:
		factorial = factorial * numero
		numero -=1
		print(factorial)

factorial_numero(4)
"""
"""
#Funciones con retorno
def factorial_numero(numero):
	factorial = 1
	while numero > 0:
		factorial = factorial * numero
		numero -=1
	return factorial

resultado = factorial_numero(4)
print(resultado)
"""
"""
def suma(valor_uno,valor_dos):
	total = valor_uno + valor_dos
	return total

total = suma(3,5)
print(total)
"""

"""
def multiples_valores():
	return "String", 1, True, 25.6

resultado = multiples_valores()
string = resultado[0]
entero = resultado[1]
print(string,entero)
"""

"""
def palindromo(frase):
	nuevo_valor = frase.replace(' ','') # Variables locales
	return nuevo_valor == nuevo_valor[::-1]

frase = 'anita lava la tina'
print(frase)
resultado = palindromo(frase)
print(frase)
print(resultado)
"""

"""
def valor_global():
	global variable_global
	variable_global = 'Cambiar Valor' # variable Local

variable_global = 'Esto es una variable Global' # variable Local

print(variable_global)
valor_global()
print(variable_global)
"""
"""
def suma(**kwargs):
	valor = kwargs.get('valor','No contiene valor')
	print(valor)

resultado = suma(valor = 'Eduardo',x = 2, y = 9, z = True)
print(resultado)
"""

mi_funcion = lambda valor_uno, valor_dos : valor_uno + valor_dos
formato = lambda sentencia : '¿{}?'.format(sentencia)
no_valor = lambda : 10
no_resultado = lambda : print('Deben de ejecutar una accion')

resultado = mi_funcion(10,20)
print(resultado)