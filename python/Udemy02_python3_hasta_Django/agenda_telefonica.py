agenda_telefonica = dict()

print ("Bienvenido a mi Agenda Telefonica...")

def imprimir_operacion(nombre_operacion):
    print ("---------- Agenda Telefonica ----------")
    print (nombre_operacion)
    print ("---------------------------------------")

def agregar_contacto():
    print()
    nombre = input("Nombre del contacto: ").capitalize()
    numero = input("Numero del contacto: ")
    agenda_telefonica[nombre] = numero
    imprimir_operacion("* Contacto Agregado")

def remover_contacto():
    nombre = input("Nombre del contacto a remover: ").capitalize()
    nombre_operacion = None

    try:
        del agenda_telefonica[nombre]
    except KeyError:
        nombre_operacion = "* Este contaacto no existe"
    else:
        nombre_operacion = "* Contacto Removido"
    imprimir_operacion(nombre_operacion)


def actualizar_contacto():
    nombre_operacion = None
    nombre = input("Nombre del contacto a actualizar: ").capitalize()
    numero = input("Nuevo Numero del contacto: ")
    agenda_telefonica[nombre] = numero
    imprimir_operacion("* Contacto Actualizado")

def ver_contacto():
    nombre = input("Nombre del contacto: ").capitalize()
    nombre_operacion = None
    
    try:
        nombre_operacion = "{} - {}".format(nombre, agenda_telefonica[nombre])
    except KeyError:
        nombre_operacion = "* Ese contacto No Existe"
    imprimir_operacion(nombre_operacion)


def ver_list_contactos():
    nombre_operacion = None

    if len(agenda_telefonica) == 0:
        nombre_operacion = "* No tienes ningun contacto"
    else:
        for contacto in agenda_telefonica:
            if nombre_operacion == None:
                nombre_operacion = "{} - {}".format(contacto, agenda_telefonica[contacto])
            else:
                nombre_operacion += "\n{} - {}".format(contacto, agenda_telefonica[contacto])
    imprimir_operacion(nombre_operacion)



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
  
