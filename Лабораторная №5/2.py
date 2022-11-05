class Vector:
    def __init__(self, *numbers: list[int] | int):
        if isinstance(numbers, int):
            numbers = [numbers]
        self.numbers = [number for number in numbers if isinstance(number, int)]

    def __str__(self):
        if len(self.numbers) == 0:
            return "Пустой вектор"
        return f"Вектор({', '.join([str(number) for number in self.numbers])})"


v1 = Vector(1, 2, 3)
print(v1)  # печатает "Вектор(1, 2, 3)"
v2 = Vector()
print(v2)  # печатает "Пустой вектор"