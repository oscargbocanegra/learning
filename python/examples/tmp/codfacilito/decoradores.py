logueado = True
usuario = "Codigofacilito"

def admin(f):
    def comprobar(*args, **kwargs):
        if logueado:
            f(*args, **kwargs)
        else:
            print "No tiene permisos de ejecutar", f.__name__
    return comprobar

def decorador(funcion):
    def funcionDecorada(*args, **kwargs):
        print "Funcion Ejecutada", funcion.__name__
        funcion(*args, **kwargs)
    return funcionDecorada

@admin
@decorador
def resta(n,m):
    print n-m

resta(3,5)
