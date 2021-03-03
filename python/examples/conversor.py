menu = """
Bienvenido al conversor de monedas 

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opcion: 
"""
opcion = input(menu)

def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuantos pesos " + tipo_pesos + " tienes? ")
    pesos =float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print ("Tienes $ " + dolares + " Dolares")    

if opcion == '1':
    conversor("Colombianos", 3875)
    
elif opcion == '2':
    conversor("Argentinos", 65)

elif opcion == '3':
    conversor("Mexicanos", 24)

else:
    print("Ingresa una opcion correcta")
