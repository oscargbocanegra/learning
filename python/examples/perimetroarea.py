# Calcular el perímetro y área de un rectángulo dada su base y su altura.

base = int(input('Introduce el valor de la base: '))
area = int(input('Introduce el valor de la altura: '))

perimetro = ((2*base) + (2*area))
area = (base * area)

print ('El perimetro es ' + str(perimetro) + ' El area es ' + str(area))