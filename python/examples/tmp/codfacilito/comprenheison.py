"""lista = []
for valor in range(0,101):
	lista.append(valor)
print(lista)
"""

lista = [valor for valor in range(0,101) if valor % 2 == 0]
#print(lista)
pass

tupla = tuple (valor for valor in range(0,101) if valor % 2 == 0)
#print(tupla)
pass

diccionario = { indice:valor for indice, valor in enumerate(lista)}
print(diccionario)