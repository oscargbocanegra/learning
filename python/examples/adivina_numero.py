import random

def run():
    numero_aleatorio = random.randint(1,100)
    numero_elegido = int(input('Elige un numero entre 1 y 100: '))
    intentos = 0
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('Busca un numero mas grande: ')
        else:
            print('Busca un numero mas pequeño: ')
        intentos +=1
        numero_elegido = int(input('Elige otro numero: '))

    if intentos == 0:
        print('Ganaste con 0 Intentos eres un Genio' )
    else:
        print('Realizaste ' +str( intentos )+ ' intentos para encontrar el Numero' )

if __name__ == '__main__':
    run()