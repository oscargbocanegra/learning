class Animal:
	volador = True

class Cocodrilo(Animal):
	def __init__(self, nombre):
		self.nombre = nombre

	@classmethod
	def new(cls, nombre):
		cls.volador = False
		return Cocodrilo(nombre)

Cocodrilo = Cocodrilo.new('coco')
print(Cocodrilo.nombre)
print(Cocodrilo.volador)