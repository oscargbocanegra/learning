import math

print "dame un mumero y te devuelvo el factorialy logaritmo  del mismo"
numero = float(raw_input())
factorial = math.factorial(math.floor(numero))
logaritmo = math.log10(math.floor(numero))

print "El logaritmo de %f es %f y su factorial redondeado hacia abajo es %d"%(numero,logaritmo,factorial)
