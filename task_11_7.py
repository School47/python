# Реализовать проект «Операции с комплексными числами».
# Создать класс «Комплексное число».
# Реализовать перегрузку методов сложения и умножения комплексных чисел.
# Проверить работу проекта.
# Для этого создать экземпляры класса (комплексные числа), выполнить сложение и умножение созданных экземпляров.
# Проверить корректность полученного результата.


class ComplexNumber:
    def __init__(self, complex_number_str):  # из строки делает комплексное число
        self.value = complex(complex_number_str)

    def __add__(self, other):
        """
        возвращает сумму комплексных чисел в виде строки
        """
        result = self.value + other.value  # тип - комплексные числа
        return ComplexNumber(str(result))  # тип строка

    def __mul__(self, other):  # умножение
        """
        возвращает произведение комплексных чисел в виде строки
        """
        result = self.value * other.value  # тип - комплексные числа
        return ComplexNumber(str(result))  # тип строка

    def __str__(self):
        return str(self.value)


x1 = ComplexNumber('1-5j')
x2 = ComplexNumber('5+8j')
print(f'x1 = {x1}')
print(f'x2 = {x2}')
summx1x2 = x1 + x2  # class Complex_number
print(f'x1 + x2 = {summx1x2}')
multiplicationx1x2 = x1 * x2  # class Complex_number
print(f'x1 * x2 = {multiplicationx1x2}')
print('*'*22+' Сложим и перемножим полученные результаты '+'*'*22)
nice_summ = summx1x2 + multiplicationx1x2 # class Complex_number
nice_multiply = summx1x2 * multiplicationx1x2 # class Complex_number
print(f'{summx1x2} + {multiplicationx1x2} = {nice_summ}')
print(f'{summx1x2} * {multiplicationx1x2} = {nice_multiply}')