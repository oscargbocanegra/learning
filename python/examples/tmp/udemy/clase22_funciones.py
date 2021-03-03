def pedir_pizza():
	print("No pudes pedir pizza".upper())

pedir_pizza()


def checar_entreda(edad):
	if edad < 18: 
		print('no puedes entrar')
	elif edad >= 21: 
		print('puedes entrar y tambien puedes beber')
	else: print('puedes entrar al bar  pero no puedes beber')

edad = 21
edad2 = 17
checar_entreda(edad)
checar_entreda(edad2)

def pedir_pizza():
	print('Pedir pizza')
