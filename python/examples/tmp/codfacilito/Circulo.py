class Circulo :
	@staticmethod
	def pi():
		return 3.1416

	def __init__(self, radio):
		self.radio = radio

	def area(self):
		return self.radio * self.radio * self.pi()

print(Circulo.pi())
circulo_uno = Circulo(7)
print(circulo_uno.area())