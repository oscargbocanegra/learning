class UnoError(Exception):
    def __init__(self,valor):
        self.valorError = valorError
    def __str__(self):
        print "No se puede dividir entre 1 el numero: ",self.valorError

print "Bienvenido"

#d = 5
#n = 1

#if n==1:
#    raise UnoError(d)

n = 1

try:
    print n/0
except TypeError:
    print "Error en tipo de dato"
except NameError:
    print "Variable no existe"
except ZeroDivisionError:
    print "No se puede dividir entre 0"
else:
    print "No hubo error"

print "Adios"
