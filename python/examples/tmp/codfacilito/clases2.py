class Usuario:
	def __init__(self, username, password, email):
		self.username = username
		self.__password = self.__generar_password(password)
		self.email = email

	def __generar_password(self, password):
		return password.upper()

	def get_password(self):
		return self.__password

eduardo = Usuario('eduardo','eduardo123','eduardo@gmail.com')
print (eduardo.username)
print (eduardo.email)
print (eduardo.get_password())
