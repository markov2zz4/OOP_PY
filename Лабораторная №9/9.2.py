class Customer:
	def __init__(self, name, balance=0):
		self.name = name
		self.balance = balance

	def withdraw(self, value):
		if self.check_type(value) and self.balance >= value:
			self.balance -= value
		else:
			raise ValueError("Сумма списания превышает баланс")

	def deposit(self, value):
		if self.check_type(value):
			self.balance += value

	def check_type(self, value):
		if isinstance(value, int | float):
			return True
		else:
			raise TypeError("Банк работает только с числами")

bob = Customer('Bob Odenkirk')
bob.deposit(200)
print(bob.balance)  # 200
bob.withdraw(150)
print(bob.balance)  # 50
#bob.deposit('hello') # TypeError: Банк работает только с числами
#bob.withdraw(300) # ValueError: Сумма списания превышает баланс