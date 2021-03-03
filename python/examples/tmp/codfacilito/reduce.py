s = ('H','o','l','a','_','M','u','n','d','o')

def concatenar(a,b):
    print a
    print b
    return a+b

sr = reduce(concatenar,s)

print type(sr)
print sr
