
class Rectangle:
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def calculate_area(self):
		return self.width * self.height

	@classmethod
	# metódo da classe chamado na classe
	# cls retorna um novo objeto da classe
	def new_squares(cls, side_length):
		return cls(side_length, side_length)

square = Rectangle.new_squares(5)
print(square.calculate_area())