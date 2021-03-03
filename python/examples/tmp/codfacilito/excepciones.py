try:
	lista = [1,2]
	print(lista[9])
except Exception as e:
	print (e)
	print ("No se obtubo el valor del indice")
finally: # si o si
	print("Por aqui pasa obligatorio")

