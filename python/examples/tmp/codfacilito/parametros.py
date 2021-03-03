import sys

if __name__ == '__main__':
	print(sys.argv)

try:
	print(2/0)
except Exception as ex:
	print("No es posinle dividir por 0")
	print("Valor excepcion " + ex)