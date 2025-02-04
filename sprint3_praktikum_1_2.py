class MushroomsCollector:
    def __init__(self):
        self.mushrooms = []
    def is_poisonous(self, mushroom_name):
        if mushroom_name == 'Мухомор':
            return True
        elif mushroom_name =='Поганка':
            return True
        return False

    def add_mushroom(self, mushroom_name):
        if self.is_poisonous(mushroom_name):
            print('Нельзя добавить ядовитый гриб')
        else:
            self.mushrooms.append(mushroom_name)

    def __str__(self):
        return ', '.join(self.mushrooms)

# Пример запуска для самопроверки


collector_1 = MushroomsCollector()
collector_1.add_mushroom('Мухомор')
collector_1.add_mushroom('Подосиновик')
collector_1.add_mushroom('Белый')
print(collector_1)

collector_2 = MushroomsCollector()
collector_2.add_mushroom('Лисичка')
print(collector_1)
print(collector_2)
