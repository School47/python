# 1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
#
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# | 31 22 |
# | 37 43 |
# | 51 86 |
#
# | 3 5 32 |
# | 2 4 6 |
# | -1 64 -8 |
#
# | 3 5 8 3 |
# | 8 3 7 1 |

from itertools import zip_longest


class Matrix:
    def __init__(self,matrix_data):
        self.matrix_data = matrix_data

    def __str__(self):
        result = ''
        for line in self.matrix_data:
            for el in line:
                result +=f'{el:02} \t'
            result += '\n'
        return result

    def __add__(self, other):
        result = Matrix([map(sum, zip_longest(*el, fillvalue=0))
                         for el in zip_longest(self.matrix_data,other.matrix_data, fillvalue=[])])
        return result

matrix_data_1 = [[3, 5 ],[8, 7 ],[3, 5 ]]
matrix_data_2 = [[31, 71, 41],[22, 43, 86],[9, 2, 1]]

matrix1 = Matrix(matrix_data_1)
matrix2 = Matrix(matrix_data_2)

print(matrix1)
print('    +     ')
print(matrix2)
print('    =     ')

matrix3 = matrix1 + matrix2
print(matrix3)