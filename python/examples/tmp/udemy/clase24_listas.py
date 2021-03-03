#formas en que se puede crear una lista

#Agregandola a una variable con corchetes
mi_lista = [1,2,3,4]
mi_lista_alfa = ['uno','dos','tres','cuatro']
print(mi_lista)

#creandole directamente en los corchetes
['A','E','I','O','U']

#otra opcion es con la funcion list y metido entre parentesis y corchetes ([])
mi_lista_omega = list(['O','M','E','G','A'])
print(mi_lista_omega)

#tambien se pueden pasar valores y este lo separa en lista
mi_lista_string = list("OSCAR GIOVANNI")
print(mi_lista_string)


#para que sume los valores a la lista se usa el valor (+=), tambien (variable = variable +)
mi_lista += [5,6]
print(mi_lista)

# para agregar un elemento a la lista se usa la funcion append
mi_lista.append(7)
print(mi_lista)

#se puede agragar una lista a la lista
mi_lista.append(mi_lista_alfa)
print(mi_lista)

#para agragar masde un elemento se usa la funcion extend
mi_lista.extend([9,10])
print(mi_lista)

#para remover los elementos se usa la siguiente funcion
mi_lista.remove(10)
print(mi_lista)

#split separa las cadenas de texto tomando como delimitador el espacio .split()
comida_favorita = "lasagna spaguetti pizza"
comida_favorita.split()
print(comida_favorita)


#tambien se puede usar un delimitador definido .split(",")
#comida_favorita_dos = ["helado", "malteada", "soda"]
#comida_favorita_dos.split(',')
#print(comida_favorita_dos)

#JOIN es una funcion que permite unir las cadenas en una sola
comida_favorita_tres = ['perro', 'hamburguesa', 'soda']
", ".join(comida_favorita_tres)
print(comida_favorita_tres)

#otra forma de usar JOIN
comida_favorita_cuatro = ['perro', 'hamburguesa', 'soda']
comida = "Mi comida favorita es: " + ", ".join(comida_favorita_cuatro)
print(comida)

