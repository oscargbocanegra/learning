my_string = "Hola mundo! 'Oscar' "
my_string = '''Este es un string que contiene
                saltos de linea'''
print(my_string)

course = "Python"
name = "Oscar"
final_mesage = "Nuevo curso de " + course + " Por " + name #1
final_mesage = "Nuevo curso de %s por %s " %(course,name) #2
final_mesage = "Nuevo curso de {} por {} ".format(course,name) #3

print(final_mesage)
