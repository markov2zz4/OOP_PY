class Person():
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    def display_person_info(self):
        print(f"Person: {self.name} {self.surname}, {self.age}")

class Company():
    def __init__(self, company_name, location):
        self.company_name = company_name
        self.location = location

    def display_company_info(self):
        print(f"Company: {self.company_name}, {self.location}")

class Employee(Person, Company):
    def __init__(self, name, surname, age, company_name, location):
        super().__init__(name, surname, age)
        
        self.company_name = company_name
        self.location = location
        

emp = Employee('Jessica', 'Smith', 28, 'Google', 'Atlanta')
emp.display_person_info()
emp.display_company_info()
