class animal:
    def __init__(self,nombre,patas,tipo):
        self.nombre = nombre
        self.patas = patas
        self.tipo = tipo

x = animal("Tomas",4,"Can")
y = animal("Hercules",4, "Pez")
print x.nombre, x.patas, x.tipo
print y.nombre, y.patas, y.tipo
