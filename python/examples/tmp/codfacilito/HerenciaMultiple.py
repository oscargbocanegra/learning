class Animal:  #Clase super padre
	@property
	def terrestre(self):
		return True

class Felino(Animal): # Clase Padre que heredo de la super clase Animal
	@property
	def garras_tactiles(self):
		return "El Felino esta Cazando"

	@property
	def cazar(self):
		return "El felino esta cazando"

class Mascota:
	nombre = '' #todas las mascotas necesitan un nombre

	def mostrar_nombre(self):
		print(self.nombre)

class Gato(Felino, Mascota): #Clase Gato que hereda de la clase padre Felino y la superclase Animal
	def gato_cazador(self):
		self.cazar()

class Jaguar(Felino): #Clase Jaguar que hereda de la clase padre Felino y la superclase Animal
	pass

gato = Gato()
jaguar = Jaguar()
felino = Felino()

gato.nombre = 'Gato con Nombre'

print(felino.garras_tactiles)
print(gato.terrestre)
print(jaguar.terrestre)
print(gato.gato_cazador)
gato.mostrar_nombre()