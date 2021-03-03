
#def pedirPizz():
#    print("Estas pidiendo pizza")
#pedirPizz()

def checarEntrada(edad):
    if edad >19:
        print ("Puedes entrar al bar".upper())
    elif edad >= 21:
        print("Tambien puedes beber")
    else:
        print("Puedes entrar pero no puedes beber")
    #print("Finalizo la funcion")

edad = 22
edad2 = 15
checarEntrada(edad)
checarEntrada(edad2)
