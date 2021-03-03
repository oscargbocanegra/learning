def filtro(elem):
    return (elem > 0)

def filtrostr(elem):
    return (elem == "o")

l = [1,-3,2,-7,-8,-9,10]
s = "Hola mundo con doble oo"

lr = filter(filtro,l)
ls = filter(filtrostr,s)
print l
print lr
print s
print ls
