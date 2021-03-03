""" Funcion que recibe funcion"""
def seleccion(operacion):
    # funcion de suma
    def suma(n,m):
        return n+m

    #funcion de multiplicacion
    def multiplicacion(n,m):
        return n*m

    if operacion == "suma":
        return suma
    elif operacion == "multi":
        return multiplicacion

fGuardada = seleccion ("multi")

print fGuardada(12,12)
