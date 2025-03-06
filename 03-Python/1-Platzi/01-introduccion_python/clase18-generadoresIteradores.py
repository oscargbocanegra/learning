# Ejemplo Iterador
my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)

#Usar Iterador
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

print('************************************')

text = "Hola Mundo"
my_iter = iter(text)
print(next(my_iter)) 

# Iterador con for
for i in my_iter:
    print('Iterando  ' + i)

print('************************************')

limit = 10

odd_itter = iter(range(1, limit+1,2))
for nun in odd_itter:
    print(nun)


