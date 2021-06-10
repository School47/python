# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.


class Worker:

    def __init__(self, name='', surname='', position=''):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            "wage": 0,
            "bonus": 0
        }

    def write_wage_and_bonus(self, put_wage, put_bonus):
        self._income['wage'] = put_wage
        self._income['bonus'] = put_bonus


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


some_worker1 = Position()
some_worker1.name = 'Владимир'
some_worker1.surname = 'Путин'
some_worker1.position = 'Президент'
some_worker1.write_wage_and_bonus(500, 125)

some_worker2 = Position('Сергей','Шойгу','Министр обороны')
some_worker2.write_wage_and_bonus(200, 50)

print(some_worker1.get_full_name())
print(some_worker1.position)
print(some_worker1.get_total_income())
print('*' * 55)

print(some_worker2.get_full_name())
print(some_worker2.position)
print(some_worker2.get_total_income())
