""" cuando usamos funciones lambda no es encesario estas funciones

#funcion a utilizar con  map() y reduce()
def suma(n,m):
    return n+m

#funcion a utilizar con filter()
def filtrar(n):
    return (n == 'o')
"""

li = [1,-2,1,-4]
lo = [5,3,6,7]
s = "Hola Mundo"

ss = lambda n,m: n+m

print map(ss, li,lo)
print filter(lambda n: n=='o',s)
print reduce(ss,lo)

"""
print map(lambda n,m: n+m,li,lo)
print filter(lambda n: n=='o',s)
print reduce(suma,lo)
"""
