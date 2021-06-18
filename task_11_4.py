# Начать работу над проектом «Склад оргтехники». Создать класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведённых типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# Продолжить работу над предыдущим заданием.
# Разработать методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру (например, словарь).
# Продолжить работу над предыдущим заданием.
# Реализовать механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.


class Warehouse:
    # подразделения компании для передачи оргтехники
    office = {}
    kitchen = {}
    workshop = {}
    department = {}
    decommissioned_equipment = {}

    def __init__(self):
        self.warehouse = {}  # склад как объект

    def add_items_to_warehouse(self, items, quantity):
        if items in self.warehouse:
            self.warehouse[items] += quantity
        else:
            self.warehouse[items] = quantity

    def del_items_from_warehouse(self, items, quantity):
        if items in self.warehouse:
            self.warehouse[items] -= quantity
        else:
            self.warehouse[items] = -quantity

    @staticmethod
    def add_items_to_some_department(some_department, items, quantity):
        if items in some_department:
            some_department[items] += quantity
        else:
            some_department[items] = quantity

    @staticmethod
    def del_items_from_some_department(some_department, items, quantity):
        if items in some_department:
            some_department[items] -= quantity
        else:
            some_department[items] = -quantity

    @classmethod
    def print_kitchen(cls):
        if len(cls.kitchen) > 0:
            result = '**** ОСТАТКИ НА kitchen **** \n'
            for key, val in cls.kitchen.items():
                result += f'{key.name}: {val} \n'
            result += '*************************** \n'
            print(result)

    @classmethod
    def print_office(cls):
        if len(cls.office) > 0:
            result = '**** ОСТАТКИ НА office **** \n'
            for key, val in cls.office.items():
                result += f'{key.name}: {val} \n'
            result += '*************************** \n'
            print(result)

    @classmethod
    def print_workshop(cls):
        if len(cls.workshop) > 0:
            result = '**** ОСТАТКИ НА workshop **** \n'
            for key, val in cls.workshop.items():
                result += f'{key.name}: {val} \n'
            result += '*************************** \n'
            print(result)

    @classmethod
    def print_department(cls):
        if len(cls.department) > 0:
            result = '**** ОСТАТКИ НА department **** \n'
            for key, val in cls.department.items():
                result += f'{key.name}: {val} \n'
            result += '*************************** \n'
            print(result)

    @classmethod
    def print_decommissioned_equipment(cls):
        if len(cls.decommissioned_equipment) > 0:
            result = '**** ОСТАТКИ НА decommissioned_equipment **** \n'
            for key, val in cls.decommissioned_equipment.items():
                result += f'{key.name}: {val} \n'
            result += '*************************** \n'
            print(result)

    @staticmethod
    def print_all_departments():
        Warehouse.print_office()
        Warehouse.print_kitchen()
        Warehouse.print_workshop()
        Warehouse.print_department()
        Warehouse.print_decommissioned_equipment()

    def __str__(self):
        result = '**** ОСТАТКИ НА СКЛАДЕ **** \n'
        for key, val in self.warehouse.items():
            result += f'{key.name}: {val} \n'
        result += '*************************** \n'
        return str(result)


class OfficeEquipment:
    def __init__(self, price=0, weight=0, name=''):
        self.price = price
        self.weight = weight
        self.name = name

    def __str__(self):
        return self.name


class Printer(OfficeEquipment):
    def __init__(self, price=0, weight=0, name='', color=False, ):
        super().__init__(price, weight, name)
        self.color = color


class Scanner(OfficeEquipment):
    def __init__(self, price=0, weight=0, name='', portable=False):
        super().__init__(price, weight, name)
        self.portable = portable


class CopyMachine(OfficeEquipment):
    def __init__(self, price=0, weight=0, name='', double_sided_copy=False):
        super().__init__(price, weight, name)
        self.double_sided_copy = double_sided_copy


printer_epson = Printer(price=14181, weight=5, name='Epson L3150', color=True)
printer_hp = Printer(price=11890, weight=3, name='HP Laser 135r', color=True)
copy_machine_xerox = CopyMachine(price=12980, weight=6, name='XEROX WorkCentre 3025, белый', double_sided_copy=False)
scanner_canon = Scanner(price=6422, weight=2, name='Canon LiDE 400', portable=False)
print('Первичное размещение оргтехники на складе:')
great_warehouse = Warehouse()

# добавляем на склад
great_warehouse.add_items_to_warehouse(printer_epson, 2)
great_warehouse.add_items_to_warehouse(printer_hp, 15)
great_warehouse.add_items_to_warehouse(scanner_canon, 9)
great_warehouse.add_items_to_warehouse(copy_machine_xerox, 3)
print(great_warehouse)

# переносим в подразделения
great_warehouse.del_items_from_warehouse(printer_epson, 1)
great_warehouse.add_items_to_some_department(Warehouse.kitchen, printer_epson, 1)

great_warehouse.del_items_from_warehouse(printer_hp, 3)
great_warehouse.add_items_to_some_department(Warehouse.office, printer_hp, 3)

great_warehouse.del_items_from_warehouse(scanner_canon, 6)
great_warehouse.add_items_to_some_department(Warehouse.office, scanner_canon, 6)

great_warehouse.del_items_from_warehouse(copy_machine_xerox, 3)
great_warehouse.add_items_to_some_department(Warehouse.office, copy_machine_xerox, 3)

great_warehouse.del_items_from_warehouse(printer_epson, 1)
great_warehouse.add_items_to_some_department(Warehouse.office, printer_epson, 1)

print('Перенесенная со склада техника:')
Warehouse.print_all_departments()

print(f'Остатки на складе после переноса оргтехники:')
print(great_warehouse)

printer_quantity = input(f'Сколько принтеров "{printer_hp}" добавим на главный склад?')
if printer_quantity.isdigit():
    #  [x] механизм валидации вводимых пользователем данных.
    great_warehouse.add_items_to_warehouse(printer_hp, int(printer_quantity))
    print(f'Остатки на складе после добавления {printer_quantity} "{printer_hp}":')
    print(great_warehouse)
else:
    print('Нужно было вводить число! принтеры не будут добавлены!')
