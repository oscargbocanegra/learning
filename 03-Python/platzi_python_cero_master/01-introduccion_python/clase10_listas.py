to_do = ["Dirigirnos al hospital", "Llamar a la familia", "Comprar medicamentos", "Descansar"]
print(to_do)
print(type(to_do))

numbers = [1,2,3,4,"Cinco"]
print(type(numbers))

mix = ["Uno",2,3.14,True, [1,2,3]]
print(type(mix))
print(len(mix))
print("Primer elemento de la lista mix: ", mix[0])
print("Segundo elemento de la lista mix: ", mix[1])
print("Ultimo elemento de la lista mix: ", mix[-1])

# Slicing
print("Primeros dos elementos de la lista mix: ", mix[0:2])

# Agregar elementos a la lista
mix.append("Nuevo elemento")
print(mix)

# Agregar elementos a la lista en una posicion especifica
mix.insert(1, "Segundo elemento")
print(mix)

numbers = [1,2,3,4,5,20,70,50,10,100]
print(numbers)
print("Mayor numero de la lista: ", max(numbers))
print("Menor numero de la lista: ", min(numbers))