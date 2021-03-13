
class Pizza:
	def __init__(self, toppings):
		self.toppings = toppings
		self._pineapple_allowed = False


	@property # Cria um atributo somente leitura
	def pineapple_allowed(self):
		return self._pineapple_allowed

	@pineapple_allowed.setter
	def pineapple_allowd(self, value):
		if value:
			password = input("enter the passwrd: ")
			if passwrd == "Sw0rdf1sh!":
				self._pineapple_allowed = value
			else:
				raise ValueError("Alert! Intruder!")

pizza = Pizza(["cheese","tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineappple_allowed)
	