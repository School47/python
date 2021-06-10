# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self,put_title=''):
        self.title = put_title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Я ручка!')


class Pencil(Stationery):
    def draw(self):
        print('Я карандашик!')



class Handle(Stationery):
    def draw(self):
        print('Я маркерок!')


nice_pen = Pen()
nice_pencil = Pencil()
nice_handle = Handle()
nice_stationary = Stationery()

nice_pen.draw()
nice_pencil.draw()
nice_handle.draw()
print('--' * 11)
nice_stationary.draw()