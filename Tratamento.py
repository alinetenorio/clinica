class Tratamento:
	
	def __init__(self, id, nome, valor):
                #id random
		self.id = id
		self.nome = nome
		self.valor = valor

	def __str__(self):
                return "Tratamento: " + self.nome + "\tValor: " + str(self.valor)
