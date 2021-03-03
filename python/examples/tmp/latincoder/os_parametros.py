from sys import argv

script, nombre, apellido, filename = argv

print "Hola %s %s como estas"%(nombre, apellido)
print "Creando el archivo %r "%filename
file = open(filename, 'w')
file.write("Este archivo fue creado a travez de python")
file.close()

print ("Proceso terminado")
