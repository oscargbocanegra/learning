class perro:
    patas = 4
    nombre = ""

    def nombre(self,n):
        self.nombre = n


mascota = perro()
mascota2 = perro()

mascota.nombre("Tom")
mascota2.nombre("Luna")

print "Tengo un perro, se llama %s y tiene %s patas"%(mascota.nombre, mascota.patas)
print "Tengo otro perro, se llama %s "%(mascota2.nombre)
