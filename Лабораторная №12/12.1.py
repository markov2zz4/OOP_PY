class Registration:
	def __init__(self, login, password):
		self.login = login
		self.password = password

	@property
	def login(self):
		return self.__login

	@login.setter
	def login(self, login):

		if not isinstance(login, str):
			raise TypeError("Логин должен быть строкой")

		if "@" not in login:
			raise ValueError("Логин должен содержать один символ '@'")
		if "." not in login[login.find("@"):]:
			raise ValueError("Логин должен содержать символ '.'")
		self.__login = login

	@staticmethod
	def is_include_digit(password):
		for i in range(len(password)):
			if password[i].isdigit():
				return True
		return False

	@staticmethod
	def is_include_all_register(password):
		for i in range(len(password)):
			if password[i].isupper():
				return True
		return False

	@staticmethod
	def is_include_only_latin(password):
		return password.isascii()

	@staticmethod
	def check_password_dictionary(password: str):
		with open('easy_passwords.txt') as f:
			if password in f.read():
				return True
		return False


	@property
	def password(self):
		return self.__password

	@password.setter
	def password(self, password):
		if isinstance(password, str):
			pass
		else: raise TypeError("Пароль должен быть строкой")

		if 4 < len(password) < 12:
			pass
		else: raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')

		if self.is_include_digit(password):
			pass
		else: raise ValueError('Пароль должен содержать хотя бы одну цифру')

		if self.is_include_all_register(password):
			pass
		else: raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')

		if self.is_include_only_latin(password):
			pass
		else: raise ValueError('Пароль должен содержать только латинский алфавит')

		if self.check_password_dictionary(password):
			raise ValueError('Ваш пароль очень прост')

		self.__password = password


# r1 = Registration('qwerty@rambler.ru', 'QwrRt124') # здесь хороший логин
# print(r1.login, r1.password) # qwerty@rambler.ru QwrRt124
# r1.login, r1.password = "r1@mail.ru", "MyPassword1"
# print(r1.login, r1.password) # r1@mail.ru MyPassword1

r1 = Registration('qwerty@rambler.ru', 'QwrRt124') # ValueError: Логин должен содержать символ .
# r1.login = 123456 # TypeError: Логин должен быть строкой
# r1.login = '123456' # ValueError("Логин должен содержать один символ '@'")
# r1.login = "Cherry@mailru" # ValueError: Логин должен содержать символ '.'

# r1.password = 43 # raise TypeError("Пароль должен быть строкой")
# r1.password = 'LoW' # raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
# r1.password = 'Versus' #ValueError: Пароль должен содержать хотя бы одну цифру
# r1.password = '123456' # ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
# r1.password = 'ХолодFr123' #ValueError: Пароль должен содержать только латинский алфавит
# r1.password = 'Qwerty123' #ValueError: Ваш пароль очень прост

r1.password = 'AbcDEf12'
print(r1.login, r1.password)