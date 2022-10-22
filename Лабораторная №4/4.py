class Stack:
	def __init__(self):

		self.values = list()

	def is_empty(self):
		return True if len(self.values) == 0 else False

	def push(self, item):
		self.values.append(item)

	def pop(self):
		return self.values.pop() if self.is_empty() != True else "Empty stack"

	def size(self):
		return len(self.values)

	def peek(self):
		if self.is_empty():
			print("Empty stack")
		else:
			return self.values[-1:]


s = Stack()
s.peek() # распечатает 'Empty Stack'
print(s.is_empty()) # распечатает True
s.push('cat') # кладем элемент 'cat' на вершину стека
s.push('dog') # кладем элемент 'dog' на вершину стека
print(s.peek()) # распечатает 'dog'
s.push(True) # кладем элемент True на вершину стека
print(s.size()) # распечатает 3
print(s.is_empty()) # распечатает False
s.push(777) # кладем элемент 777 на вершину стека
print(s.pop()) # удаляем элемент 777 с вершины стека и печатаем его
print(s.pop()) # удаляем элемент True с вершины стека и печатаем его
print(s.size()) # распечатает 2