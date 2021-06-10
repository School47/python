# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
# А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
#  При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

class Car:
    def __init__(self):
        self.speed=0
        self.color = ''
        self.name = ''
        self.is_police= False

    def go(self):
        print('Машина поехала')


    def stop(self):
        print('Машина остановилась')

    def turn(self,direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость авто: {self.speed}')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Текущая скорость авто: {self.speed},Скорость превышает 60 км/ч!')
        else:
            print(f'Текущая скорость авто: {self.speed}')


class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Текущая скорость авто: {self.speed},Скорость превышает 40 км/ч!')
        else:
            print(f'Текущая скорость авто: {self.speed}')


class PoliceCar(Car):
    def __init__(self):
        self.is_police = True

town_bus = TownCar()
town_bus.name  = 'Автобус'
town_bus.speed = 61
town_bus.color = 'red'

lambo = SportCar()
lambo.name = 'lamborghini'
lambo.speed = 215
lambo.color = 'black'

bobcat = WorkCar()
bobcat.name = 'Погрузчик'
bobcat.speed = 41
bobcat.color = "yellow"

police = PoliceCar()
police.name = 'Полицейская машина'
police.speed = 90
police.color = 'red and blue'

print(town_bus.name)
town_bus.go()
town_bus.turn('налево')
town_bus.show_speed()
print('--'*25)
print(police.name)
police.stop()
police.show_speed()
print('--'*25)
print(lambo.name)
lambo.go()