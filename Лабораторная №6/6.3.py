class Building:
    def __init__(self, floor):
        self.floor = dict()
        for i in range(floor):
            self.floor[i] = "_"

    def __setitem__(self, key, value):
        if isinstance(key, int) and key >= 0:
            self.floor[key] = value

    def __getitem__(self, key):
        return self.floor[key]

    def __delitem__(self, key):
        self.floor[key] = None

iron_building = Building(22) # Создаем здание с 22 этажами
iron_building[0] = 'Reception'
iron_building[1] = 'Oscorp Industries'
iron_building[2] = 'Stark Industries'
print(iron_building[2])
del iron_building[2]
print(iron_building[2])