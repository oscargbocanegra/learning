menu = """
Bienvenido al conversor de monedas 

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opcion: 
"""
opcion = input(menu)

if opcion == '1':
    pesos = input("¿Cuantos pesos colombianos tienes? ")
    pesos =float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print ("tienes $ " + dolares + " Dolares")    
elif opcion == '2':
    pesos = input("¿Cuantos pesos Argentinos tienes? ")
    pesos =float(pesos)
    valor_dolar = 65
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print ("tienes $ " + dolares + " Dolares")    
elif opcion == '3':
    pesos = input("¿Cuantos pesos Mexicanos tienes? ")
    pesos =float(pesos)
    valor_dolar = 24
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print ("tienes $ " + dolares + " Dolares")    
else:
    print("Ingresa una opcion correcta")
