"""Clase Humano que contendra el constructor y metodos de la Clase"""
class Humano:
    def __init__(self,edad):
        self.edad = edad
        print "Edad de ",edad

    def hablar(self,mensaje):
        print mensaje

"""subclase Ingeniero de sistemas que hereda de la clase Humano"""
class IngSistemas(Humano):
    def __init__(self):
        print "Hola este es el constructor de Ing de Sistemas"

    def programar(self,lenguaje):
        print "voy a programar en ", lenguaje

"""Sub clase licenciado en derecho que hereda de la clase humano"""
class LicDerecho(Humano):
    def estudiarCaso(self, de):
        print "Debo estudiar el caso de ", de

""" Multiclese que hereda de las 2 clases"""
class estudioso(IngSistemas, LicDerecho):
    pass

"""Impresiones por pantalla"""
pedro = IngSistemas()
pedro.hablar("Bienvenido metodo hablar")
raul = LicDerecho(26)
pedro.programar("Python")

juan = estudioso()
juan.estudiarCaso("Pedro")
