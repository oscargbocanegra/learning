class Circulo:
	pi = 3.1416

	def __init__(self, radio):
		self.radio = radio

	def area(self):
		return self.radio * self.radio * self.pi

Circulo_uno = Circulo(4)
Circulo_dos = Circulo(3)
		
print(Circulo.pi) #No es necesario crear un objeto para usar PI
print(Circulo_uno.area())