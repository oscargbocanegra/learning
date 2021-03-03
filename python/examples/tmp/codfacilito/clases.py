class Lapiz:
	color = 'Amarillo'
	contiene_borrador = True
	usa_grafito = True

	#estos son metodos
	def dibujar(self):
		print("El lapiz esta dibujando")

	def borrar(self):
		if self.es_valido_para_borrar():
			print("El lapiz esta borrando")
		else:
			print("no es posible borrar")

	def es_valido_para_borrar(self):
		return self.contiene_borrador

lapiz_generico = Lapiz()
lapiz_generico.dibujar()
