class Vehicle:
	def __init__(self, name, mileage, capacity):
		self.name = name
		self.mileage = mileage
		self.capacity = capacity
	def fare(self):
		return self.capacity*100
	def display(self):
		print(f"Total name - {self.name}, mileage - {self.mileage}, fare is {self.fare()}")

class Bus(Vehicle):
	def __init__(self, name, mileage):
		super().__init__(name, mileage, 50)
	def fare(self):
		return super().fare() * 0.1

class Taxi(Vehicle):
	def __init__(self, name, mileage):
		super().__init__(name, mileage, 4)
	def fare(self):
		return super().fare() * 0.35

sc = Vehicle('Scooter', 100, 2)
sc.display()
merc = Bus("Mercedes", 120000)
merc.display()
polo = Taxi("Volkswagen Polo", 15000)
polo.display()