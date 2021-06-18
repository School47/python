# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый — с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй — с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
import re


class Data:
    def __init__(self, data_in_str):
        if Data.is_data_valid(data_in_str):  # проверка на валидность даты
            self.data = data_in_str
            self.valid_data = True
        else:
            print(f'Дата {data_in_str} задана неверно')
            self.data = data_in_str  # но все равно принимаем
            self.valid_data = False  # c оговоркой что дата не айс.

    @classmethod
    def data_to_number(cls, data_input):
        data_list = data_input.split(
            '-')  # тут данные всегда валидные, мы до этого проверяли их методом is_data_valid()
        day, month, year = data_list
        return int(day + month + year) # [x] преобразовать дату в число.

    @staticmethod
    def is_data_valid(some_data):
        if re.fullmatch(r'\d{1,2}-\d{1,2}-\d{4}', some_data):  # вроде похоже на дату, проверим значения чисел
            data_list = some_data.split('-')  # сплитим числа в лист
            day, month, year = data_list
            if int(day) >= 0 and int(day) <= 31 and int(month) >= 1 and int(month) <= 12:
                return True
            else:
                return False
        else:
            return False


some_data_in_str1 = '11-12-2021'
some_data_in_str2 = '22-21-1999'
some_data_in_str3 = '11-12-2x2o'
some_data_in_str4 = '1122-1234-2x2o'
some_data_in_str5 = '11-12-2x2o-1'
some_data_in_str6 = '10-7-2049'

list_all_datas = [some_data_in_str1, some_data_in_str2,
                  some_data_in_str3, some_data_in_str4, some_data_in_str5, some_data_in_str6]
data_class_lists = [Data(ex_data) for ex_data in list_all_datas]  # создаем экземпляры класса для всех дат

data_digits_lists = [Data.data_to_number(ex_data.data) for ex_data in data_class_lists if ex_data.valid_data]
# если дата валидная, создаем из даты число.

print('Список дат, которые были введены верно, преобразованные в  "число": ')
print(data_digits_lists)
