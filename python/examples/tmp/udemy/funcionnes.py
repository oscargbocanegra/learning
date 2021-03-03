def checar_entrada(edad):
    if edad < 18:
        print ("No puedes entrar")
    elif edad >= 21:
        print ("Puedes entrar al bar y tambien puedes beber".upper())
    else:
        print ("Puedes entrar al bar pero no puedes beber")

edad = 21
edad_2 = 17

checar_entrada(edad)

checar_entrada(edad_2)
