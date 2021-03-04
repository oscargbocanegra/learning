def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }

    #Imprimiendo cada llave del dicionario
    # print(mi_diccionario['llave1'])
    # print(mi_diccionario['llave2'])
    # print(mi_diccionario['llave3'])

poblacion_paises = {
    'Argentina': 44938435,
    'Brazil': 210987435,
    'Colombia': 50976342,
}

# Metodo for imprimiendo la lista por la llave
for pais in poblacion_paises.keys():
    print(pais)

# Metodo for imprimiendo la lista por el valor
for pais in poblacion_paises.values():
    print(pais)

# Metodo for imprimiendo la lista por los dos valores
for pais, poblacion in poblacion_paises.items():
    print(pais + ' tiene ' + str( poblacion ) + ' habitantes')


if __name__ == '__main__':
    run()