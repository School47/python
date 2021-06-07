from functools import wraps
import math


def val_checker(x):
    def _logger(func):
        @wraps(func) # маскировка
        def wrapper(*args):
            input_correct = x(args[0])
            try:
                if input_correct: # проверка аргумента
                    result = func(*args) # аргумент прошел проверку
                else:
                    raise ValueError #аргумент не прошел проверку, вызываем ошибку.
            except ValueError :
                print(f'ValueError: wrong value: {args[0]}')
                result = None
            return result

        return wrapper

    return _logger


@val_checker(lambda x: x > 0)
def calc_sqrt(x):  # Возвращает квадратный корень числа Х, либо None, если x отрицательное
    return math.sqrt(x)


a = calc_sqrt(9)
print(a)
b = calc_sqrt(-9)
print(b)

print(f'{calc_sqrt} <-- работа декоратора замаскирована')
