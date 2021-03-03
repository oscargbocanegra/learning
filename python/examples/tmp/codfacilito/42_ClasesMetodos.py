class Usuario:
	def __new__(cls):
		print("Este metodo es el primero que se ejecuta")
		return super().__new__(cls)

	def __init__(self):
		print("Este metodo es el segundo que se ejecuta")

	def __str__(self):
		return "Esto se imprime cuando intento mostrar un objeto."

	def __getattr__(self, nombre):
		print("Aqui mostramos que no se encontro el atributo")
		self.otros_metodos()

	def otros_metodos(self):
		print("Otro metodo")

usuario = Usuario()
print(usuario)
print(usuario.apellido)
