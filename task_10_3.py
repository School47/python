# Осуществить программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс «Клетка».
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
# деление (__floordiv____truediv__()).
# Эти методы должны применяться только к клеткам и выполнять увеличение,
# уменьшение, умножение и округление до целого числа деления клеток соответственно.

class Cell:
    def __init__(self,quantity):
        self.quantity = quantity

    def __add__(self, other):
        return self.quantity + other.quantity

    def __sub__(self, other):
        if self.quantity > other.quantity:
            return self.quantity - other.quantity
        else: return 'нуль или меньше'

    def __mul__(self, other):
        return self.quantity * other.quantity
    def __floordiv__(self, other):
        return self.quantity // other.quantity


    def make_order(self,num_cells_in_row):
        total_rows = self.quantity // num_cells_in_row
        last_row = self.quantity % num_cells_in_row
        result = ('*'*num_cells_in_row+"\n")*total_rows+'*'*last_row
        return result





cell1 = Cell(15)
cell2 = Cell(7)
cells_in_a_row = 6

print(f'Первая клетка состоит из {cell1.quantity} ячеек')
print(f'Вторая клетка состоит из {cell2.quantity} ячеек')

print(f'Сумма клеток равна {cell1 + cell2}')
print(f'Разность клеток равна: {cell1 - cell2}')
print(f'Произведение клеток равно {cell1 * cell2}')
print(f'Округление до целого числа деления клеток: {cell1 // cell2}')
print(f'Делим первую клетку, состоящую из {cell1.quantity} ячеек на {cells_in_a_row} клеток в ряду')
print(cell1.make_order(cells_in_a_row))