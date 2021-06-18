# Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверить его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
import time
import random


class Bcolors:  # простой класс для хранения стилей строк.
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class OwnError(Exception):  # собственный класс-исключение
    def __init__(self, txt):
        self.txt = txt


def Special_print(string_for_print, speed=0.0999, need_line_break=True):
    """
    Выводит строку как печатная машинка
    :param string_for_print: то что надо напечатать в виде строки
    :param speed: скорость печатания знака в секундах
    need_line_break : перенос строки в конце
    :return: в замен ничего не дает
    """
    for every_letter in string_for_print:
        print(every_letter, end='')
        time.sleep(speed)
    if need_line_break:
        print('')


number_for_punishment = random.randint(1, 999)
input_data = '0'
while input_data != '':
    input_data = input(f'На что будем делить {number_for_punishment}? пустое значение - выход:')
    try:
        if input_data == '':
            Special_print('Выходим!')
            exit(666)
        input_data = int(input_data)
        if input_data == 0:  # пользователь решил делить на ноль О_О!!!
            raise OwnError(' На ноль делить нельзя!')  # вызываем собственный класс-исключение
    except ValueError:
        print('Это не число')
    except OwnError as err:
        print(err)
    else:
        print(f'Сейчас разделим {number_for_punishment} на {input_data}, держитесь!', end='')
        time.sleep(random.randint(1, 999) / 1000)
        if random.randint(0, 1):
            Special_print(' ... Разгон процессора на повышенные частоты...', 0.0333, False)
        time.sleep(random.randint(1, 999) / 1000)
        if random.randint(0, 1):
            Special_print(' ... Подключение математического сопроцессора...', 0.0333, False)
        print('')
        result = number_for_punishment / input_data
        time.sleep(random.randint(1, 999) / 1000)
        print(f'{Bcolors.BOLD}{Bcolors.OKGREEN}\t \t \t \t \t \tРезультат деления: ', end='')
        time.sleep(random.randint(1, 999) / 1000)
        Special_print(str(result), 0.2345)
        print(f'{Bcolors.ENDC}', end='')
