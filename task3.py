class Tomato:
    states = {0:['0-я стадия : возраст - 45 дней, цветение'],
              1:['1-я стадия : возраст - 55 дней, цвет - зеленый'],
              2:['2-я стадия : возраст - 70 дней, цвет - бурый'],
              3:['3-я стадия : возраст - 85 дней , цвет - розовый'],
              4:['4-я стадия - "томат созрел" : возраст - 95 дней, цвет - красный']}
    def __init__(self, index):
        self._index = index
        self._state = 0
    def grow(self):
        self._change_state()
    def is_ripe(self):
        if self._state == 4:
            print(f'Томат {self._index + 1} созрел')
            return True
        print(f'Томат {self._index + 1} на стадии созревания')
        return False
    def _change_state(self):
        if self._state < 4:
            self._state += 1
        self._print_state()
    def _print_state(self):
            print(f'Томат {self._index + 1} на {Tomato.states[self._state]}')
class TomatoBush:
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(0, num)]
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()
    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])
    def give_away_all(self):
        self.tomatoes = []
class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant
    def work(self):
        print('Садовник поливает и удобряет томаты')
        self._plant.grow_all()
        print('Садовник закончил свою работу')
    def harvest(self):
        print('Садовник начинает сбор урожая томатов')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Все томаты собраны. Садовник закончил свою работу.')
        else:
            print('Томат еще не зрелый!')
    @staticmethod
    def knowledge_base():
        print('Краткая справка по выращиванию томатов:\n'
              'На урожай томатов влияет выбор сорта томатов, условия в которых растет высаженная рассада, правильный \n'
              'и своевременный полив и своевременная подкормка. Температура при выращивании томатов не должна превышать 30 С,\n'
              'важно достаточное проветривание. При соблюдении всех этих рекомендаций Вы получите богатый урожай томатов!\n'
              'Список сортов томатов:\n'
              '1.Аврора\n'
              '2.Блоссом\n'
              '3.Урал\n')
Gardener.knowledge_base()
delicious_tomato = TomatoBush(int(input('Напишите номер сорта томата, который Вас интересует: ')))
gardener = Gardener('Андрей', delicious_tomato)
gardener.work()
gardener.work()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()
