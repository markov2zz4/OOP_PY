class File:
	def __init__(self, name):
		self.name = name
		self.in_trash = False
		self.is_deleted = False

	def restore_from_trash(self):
		print(f'Файл {self.name} восстановлен из корзины')
		self.in_trash = False

	def remove(self):
		print(f'Файл {self.name} был удален')
		self.is_deleted = True

	def read(self):
		if self.is_deleted:
			print(f'ErrorReadFileDeleted({self.name})')
			return
		elif self.in_trash:
			print(f'ErrorReadFileTrashed({self.name})')
			return
		print(f'Прочитали все содержимое файла {self.name}')

	def write(self, content):
		if self.is_deleted:
			print(f'ErrorWriteFileDeleted({self.name})')
			return
		elif self.in_trash:
			print(f'ErrorWriteFileTrashed({self.name})')
			return
		print(f'Записали значение {content} в файл {self.name}')

class Trash:
	content = []

	@staticmethod
	def add(file):
		if isinstance(file, File):
			Trash.content.append(file)
			file.in_trash = True
		else:
			print('В корзину добавлять можно только файл')

	@staticmethod
	def clear():

		print('Очищаем корзину')
		for i in range(len(Trash.content)):
			File.remove(Trash.content[len(Trash.content) - 1 - i])
		Trash.content.clear()
		print('Корзина пуста')

	@staticmethod
	def restore():
		print("Восстанавливаем файлы из корзины")
		if len(Trash.content) > 0:
			try:
				for i in range(len(Trash.content)):
					File.restore_from_trash(Trash.content[len(Trash.content) - 1 - i])
					Trash.content[len(Trash.content) - 1 - i].in_trash = False
			except IndexError:
				print("Корзина пуста")
		else:
			print("Корзина пуста")
			return

file1 = File("Trojan")
file2 = File("Cleaner")

file1.write("someContent4file1")
file2.write("someContent4file2")

file1.read()
file2.read()

file1.remove()
file2.remove()

file1.restore_from_trash()
file2.restore_from_trash()

Basket = Trash()

Trash.add(file1)

print()
Trash.add(file2)
Trash.clear()