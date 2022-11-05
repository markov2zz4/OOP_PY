class Person:
    def __init__(self, name: str, surname: str, gender: str = "male"):
        self.name = name
        self.surname = surname
        self.gender = "male" if gender not in ["male", "female"] else gender

    def __str__(self):
        if self.gender == "male":
            return f"Гражданин {self.surname} {self.name}"
        else:
            return f"Гражданка {self.surname} {self.name}"

p1 = Person('Maddison', 'Cynthia', 'female')
print(p1) # печатает "Гражданка Cynthia Maddison"
p2 = Person('Zoe', 'Amber', 'female')
print(p2) # печатает "Гражданка Amber Zoe"
p3 = Person('Oscar', 'Smith', True)# печатает "Значение не передано."
print(p3) # печатает "Гражданин Smith Oscar"