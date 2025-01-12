x = 10
if x > 5:
    print("x es mayor a 5")
else:
    print("x es menor a 5")
print("Fin del programa")

is_member = True
age = 18

# If anidado
if is_member:
    if age >= 15:
        print("Puede ingresar")

# Juego piedra, papel o tijera
opciones = ["piedra", "papel", "tijera"]

player1 = input("Elige piedra, papel o tijera: ")
player2 = input("Elige piedra, papel o tijera: ")
if player1 == player2:
    print("Empate")
elif (player1 == "piedra" and player2 == "tijera") or (player1 == "papel" and player2 == "piedra") or (player1 == "tijera" and player2 == "papel"):
    print("Jugador 1 gana")
elif (player2 == "piedra" and player1 == "tijera") or (player2 == "papel" and player1 == "piedra") or (player2 == "tijera" and player1 == "papel"):
    print("Jugador 2 gana")
else:
    print("Opción no válida")