<<<<<<< HEAD
dc={"clave1":[1,2,3],"clave2":2,"clave3":True}

print dc["clave1"]
=======
#Los diccionarios no se rigen por un indice, las claves deben ser inmutables, si existen 2 llaves iguales toma el ultimo valor 
diccionario = {'a': 55, 'b':"diccionario", 5:"estring", 'a': False} # Las claves deben ser inmutables
#print(diccionario)

diccionario ['a'] = 'nuevo valor' # Creamos clave/valor
#print(diccionario)

diccionario ['c'] = 'nuevo valor' # si la llave se encuentra la actualiza de lo contrario la crea
#print(diccionario)

valor = diccionario.get('a',False) # Get obtener los valores

#print(diccionario)
#print(valor)

del diccionario[5] #Del opcion para eliminar
#print(diccionario)

#llaves = diccionario.keys()#Objeto iterables 
#llaves = list(diccionario.keys())#Objeto iterables
#llaves = tuple(diccionario.keys())#Objeto iterables
#valores = list(diccionario.values())
#print(llaves)
#print(valores)

diccionario_dos = {'g': 56, 'h':57} 
print(diccionario)
print(diccionario_dos)
diccionario.update(diccionario_dos) #Incrementar un diccionario a partir de otro
print(diccionario)
>>>>>>> master
