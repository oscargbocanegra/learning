course = 'curso'
my_string = 'codigo facilito'
result = '{a} de {b}'.format(a = course, b = my_string)
print (result)

#metodo lower que estandariza todo en minusculas
#result = result.lower()
#print ("Metodo minusculas " + result)

#metodo upper que estandariza todo en MAYUSCULAS
#result = result.upper()
#print ("Metodo Mayusculas " + result)

#metodo title que pone string como titulo
#result = result.title()
#print ("Metodo titulo " + result)

#Metodos de busqueda
#pos = result.find('codigo')
#print(pos)
#print(result[9])
#conteo = result.count('c')
#print(conteo)

#Metodo de sustitucion
new_string = result.replace('c','x')
print(new_string)

#Metodo split que regresa una lista seccionada
new_string = result.split(' ')
print(new_string)


