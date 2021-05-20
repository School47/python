# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
#
# Если перевод сделать невозможно, вернуть None.
# Подумайте, как и где лучше хранить информацию, необходимую для перевода: какой тип данных выбрать,
# в теле функции или снаружи.
#
# *(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv():
# реализовать корректную работу с числительными, начинающимися с заглавной буквы — результат
# тоже должен быть с заглавной. Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"
# one two three four
numbers = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven ': 'семь',
    'eight': 'восемь',
    'nine ': 'девять',
    'ten': 'десять',
    'Zero': 'Ноль',
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
    'Five': 'Пять',
    'Six': 'Шесть',
    'Seven ': 'Семь',
    'Eight': 'Восемь',
    'Nine ': 'Девять',
    'Ten': 'Десять'
}


def num_translate_adv(input_number):
    """Translate english number to russian"""
    return numbers.get(input_number)


english_number = input('Введите число от 0 до 10 английскими буквами: ')
print(num_translate_adv(english_number))
