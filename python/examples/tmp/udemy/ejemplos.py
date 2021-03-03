import os
from datetime import date

password = input("Escriba un password: ")
loop = "si"

artistas = ["messi", "pikachu", "Kamisama", "pegaso", "cisne"]

if password == "colombia":
    while loop == "si" or loop == "SI":
        year = int(input("anio de nacimiento: "))
        month = input("mes de bcimiento: ").lower()
        day = int(input("dia de nacimiento: "))
        fecha = (str(day) + "/" + month + "/" + str(year))
        hoy = date.today()
        esteanio = hoy.year
        os.system("cls")
        edad = esteanio - year
        print("tu fecha de nacimiento es: " + fecha)
        print("Este anio tendras: " + str(edad) + "anios")

        if (month == "diciembre" and day >= 22) or (month == "enero" and day <= 19):
            print("Tu signo es capricornio")
            for name in artistas:
                print(name)

        loop = input("Desea continuar con el ciclo")
