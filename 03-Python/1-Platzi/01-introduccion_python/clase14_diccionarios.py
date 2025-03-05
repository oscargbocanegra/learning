numbers = {1:"uno", 2:"dos", 3:"tres"}
print(numbers[2])
print(numbers.get(3, "No se encuentra el valor")) # Si no encuentra el valor, retorna el valor por defecto

information = { "name": "Juan",
                "age":22,
                "altura":1.65,
                "cursos": ["Python", "Django", "JavaScript"]}
print(information)
del information["altura"]
print(information)
clave = information.keys()
print(clave)
values = information.values()
print(values)
items = information.items()
print(items)