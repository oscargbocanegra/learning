class Prueba(object):
    def __init__(self):
        self.__privado = "soy privado"
        self.privado = "soy publico"

    def __metodoPrivado(self):
        return "soy metodo privado"

    def metodoPublico(self):
        print "soy metodo publico"

    def getPrivado(self):
        return self.__privado

    def setPrivado(self,valor):
        self.__privado = valor


obj = Prueba()
#print obj.privado
#print obj.__privado
#obj.metodoPublico()
#obj.__metodoPrivado()
obj.setPrivado("Tengo nuevo valor")
print obj.getPrivado()
