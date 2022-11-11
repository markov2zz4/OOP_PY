# Для этого в классе Building должно быть реализованы
# 1. метод __init__, который принимает количество этажей в здании
# 2. метод __setitem__, который закрепляет за определенным этажом компанию. Если этаж был занят другой компанией, нужно заменить название другой компанией
# 3. метод __getitem__, который возвращает название компании с этого этажа. В случае, если этаж пустует, следует вернуть None
# 4. метод __delitem__, который высвобождает этаж
# В этом задании вы сами решаете какие атрибуты создавать внутри класса, главное реализовать магические методы из списка выше

class Building:
    def __init__(self, floor):
        self.floor = dict()
        for i in range(floor):
            self.floor[i] = "_"

    def __setitem__(self, key, value):
        if(isinstance(key, int) and key >= 0):
            self.floor[self.key] = self.value



    def __getitem__():
        pass
    def __delitem__():
        pass

iron_building = Building(22) # Создаем здание с 22 этажами
iron_building[0] = 'Reception'
iron_building[1] = 'Oscorp Industries'
iron_building[2] = 'Stark Industries'
# print(iron_building[2])
# del iron_building[2]
# print(iron_building[2])