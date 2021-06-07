from functools import wraps

def type_logger(func):

    @wraps(func) # маскировка
    def wrapper(*args, **kwargs):
        result = func(*args,**kwargs)
        all_types=''
        for arg in args: #все позиционные аргументы
             all_types += f'{arg}:{type(arg)} '
        for val in kwargs.values(): # все именнованные аргументы из словаря
            all_types += f'{val}:{type(val)} '
        print(f' {func.__name__}({all_types}) Тип значения функции  - {type(result)}, результат:{result}')
        return result

    return wrapper


@type_logger
def calc_cube(x, bar=[1], height=('very','high'), y=3):
   bar.append(5)#имитируем бурную деятельность
   zz=height #имитируем бурную деятельность
   zz='' #имитируем бурную деятельность
   return x ** y

a = calc_cube(5, bar=[2], height=(1,3), y=2)
print(f'Печатаем функцию - {calc_cube} <-- работа декоратора замаскирована с помощью @wraps')