# Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H соответственно.

# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания.
# Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.
from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self,param):
        self.param = param

    @property #будем обращаться к методу как к атрибуту
    @abstractmethod #потомки обязаны прописать методы
    def need_material(self):
        pass

    def __add__(self,other):
        return self.need_material + other.need_material


    def __str__(self):
        return str(self.param)

class Coat(Clothes):
    @property
    def need_material(self):
        return self.param / 6.5 + 0.5


class Costume (Clothes):
    @property
    def need_material(self):
        return (2 * self.param + 0.3)

coat = Coat(46)
costume = Costume(175)

print(f'Размер пальто:{coat}')
print(f'Рост для костюма:{costume}')
print(f'Для пальто надо материала: {coat.need_material}')
print(f'Для костюма надо материала: {costume.need_material}')

print(f'Всего надо материала для пальто и костюма: {costume + coat}') #при сложении классов складываем требуемый материал.

