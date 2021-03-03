class Properties:
	def __init__(self, username, password, email):
		self.username = username
		self.__password = self.__generar_password(password)
		self.email = email

	def __generar_password(self, password):
		return password.upper()

	@property
	def password(self):
		return self.__password

	@password.setter
	def password(self, valor):
		self.__password = self.__generar_password(valor)

eduardo = Properties('oscar', 'oscar123', 'oscar@mail.com')
print(eduardo.password)
eduardo.password = 'Nuevo Password'
print (eduardo.password)