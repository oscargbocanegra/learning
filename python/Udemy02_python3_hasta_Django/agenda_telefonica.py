agenda_telefonica = dict()

print ("Bienvenido a mi Agenda Telefonica...")

def agregar_contacto():
    print()
    nombre = input("Nombre del contacto: ").capitalize()
    numero = input("Numero del contacto: ")
    agenda_telefonica[nombre] = numero
    print('\n----- Agenda Telefonica ------ \n * Contacto Agregado \n------------------------------')

def remover_contacto():
    print()
    nombre = input("Nombre del contacto a remover: ").capitalize()

    try:
        del agenda_telefonica[nombre]
    except KeyError:
        print('\n----- Agenda Telefonica ------ \n * Este contaacto no existe \n------------------------------')
    else:
        print('\n----- Agenda Telefonica ------ \n * Contacto Removido \n------------------------------')


def actualizar_contacto():
    print()
    nombre = input("Nombre del contacto a actualizar: ").capitalize()
    numero = input("Nuevo Numero del contacto: ")

    agenda_telefonica[nombre] = numero
    print('\n----- Agenda Telefonica ------ \n * Contacto Actualizado \n------------------------------')

def ver_contacto():
    nombre = input("Nombre del contacto: ").capitalize()
    
    try:
        print (f'\n----- Agenda Telefonica ------ \n{nombre}  --  {agenda_telefonica[nombre]} \n------------------------------')
    except KeyError:
        print('\n----- Agenda Telefonica ------ \n * Ese contacto No Existe \n------------------------------')

def ver_list_contactos():
    print()
    if len(agenda_telefonica) == 0:
        print('\n----- Agenda Telefonica ------ \n * No tienes ningun contacto \n------------------------------')
    else:
        print('----- Agenda Telefonica ------')
        for contacto in agenda_telefonica:
            print ( f'{contacto} --  {agenda_telefonica[contacto]}')
        print('------------------------------')



while True:
    print()
    print ("1 - Agregar un contacto")
    print ("2 - Remover un contacto")
    print ("3 - Actalizar contactos")
    print ("4 - Ver un contacto")
    print ("5 - Ver todos los contactos")
    print ("6 - Salir")
    print()

    try:
        operacion = int(input("Escoja Opcion : "))
    except ValueError:
        print('\n----- Agenda Telefonica ------ \n * Selecciona un numero de 1 a 6 \n------------------------------')
    else:
        if operacion == 1:
            agregar_contacto()
        elif operacion == 2:
            remover_contacto()
        elif operacion == 3:
            actualizar_contacto()
        elif operacion == 4:
            ver_contacto()
        elif operacion == 5:
            ver_list_contactos()
        elif operacion == 6:
            break
        else:
            print('\n----- Agenda Telefonica ------ \n * Operacion Desconocida \nIntente nuevamente de 1 a 6 \n------------------------------')

print('\n----- Agenda Telefonica ------ \n * Gracias por usar nuestro servicio de Agendas Telefonicas \n------------------------------')
  
