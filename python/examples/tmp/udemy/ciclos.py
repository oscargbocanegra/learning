manzana = 10
lista_numeros = [1,2,3,4,5,6,7,8,9]

def comer(manzana):
    while manzana > 0:
        print("Me estoy comiendo la manzana # " + str(manzana))
        manzana -= 1
    print("Me quede sin manzanas")

def listanumeros_for(lista_numeros):
    for numero in lista_numeros:
        print ("El numero es " + str(numero))
    print ("No hay mas")


def listanumeros_for_break(lista_numeros):
    for numero in lista_numeros:
        if numero == 7:
            break
        print ("El numero es " + str(numero))
    print ("Es igual a 7 y break rompe el ciclo")

def listanumeros_for_continue(lista_numeros):
    for numero in lista_numeros:
        if numero == 7:
            continue
        print ("El numero es " + str(numero))
    print ("Es igual a 7 y continue salta el numero ")


comer(manzana)
listanumeros_for(lista_numeros)
listanumeros_for_break(lista_numeros)
listanumeros_for_continue(lista_numeros)
    