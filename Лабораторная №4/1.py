class Laptop:
	def __init__(self, brand, model, price):
		self.brand = brand
		self.model = model
		self.price = price
	def laptop_name(self):
		print(f"Стоимость {self.brand} {self.model} составляет {self.price} рублей")

acer = Laptop('acer', 'A315-23-R2PW', 27_000)
acer.laptop_name()
