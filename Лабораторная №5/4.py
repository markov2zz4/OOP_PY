class Quadrilateral:
    def __init__(self, width: float, height: float = None):
        self.width = width
        self.height = width if height is None else height

    def __str__(self):
        if self.width == self.height:
            return f"Квадрат размером {self.width}х{self.height}"
        return f"Прямоугольник размером {self.width}х{self.height}"

    def __bool__(self):
        return self.width == self.height

q1 = Quadrilateral(10)
print(q1) # печатает "Квадрат размером 10х10"
print(bool(q1)) # печатает "True"
q2 = Quadrilateral(3, 5)
print(q2) # печатает "Прямоугольник размером 3х5"
print(q2 == True) # печатает "False"