class NewInt(int):
    def __init__(self, value):
        self.value = value
    
    def repeat(self, n = 1):
        newnum = ""
        for _ in range(n):
            newnum += str(self.value)
        return newnum
    
    def to_bin(self):
        return f"{self.value:0b} - двоичное представление числа {self.value}"


a = NewInt(9)

print(a.repeat()) # печатает число 9
d = NewInt(a + 5)
print(d.repeat(3)) # печатает число 141414
b = NewInt(NewInt(7) * NewInt(5))
print(b.to_bin()) # печатает 100011 - двоичное представление числа 35
