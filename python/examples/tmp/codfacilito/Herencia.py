class Animal:  #Clase super padre
	@property
	def terrestre(self):
		return True

class Felino(Animal): # Clase Padre que heredo de la super clase Animal
	@property
	def garras_tactiles(self):
		return "El Felino esta Cazando"

	def cazar(self):
		print("El felino esta cazando")

class Gato(Felino): #Clase Gato que hereda de la clase padre Felino y la superclase Animal
	def gato_cazador(self):
		print("El gato va a cazar con la clase del felino")
		self.cazar()

class Jaguar(Felino): #Clase Jaguar que hereda de la clase padre Felino y la superclase Animal
	pass

gato = Gato()
jaguar = Jaguar()
felino = Felino()

print(felino.garras_tactiles)
print(gato.terrestre)
print(jaguar.terrestre)
print(gato.gato_cazador)