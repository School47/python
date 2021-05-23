# 2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
# и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
# В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
# Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
# Можно ли, используя только методы класса str, решить поставленную задачу?
# Функция должна возвращать результат числового типа, например float.
# Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
# Сильно ли усложняется код функции при этом?
# Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
# Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
# В качестве примера выведите курсы доллара и евро.
# 3. * (вместо 2) Доработать функцию currency_rates():
# теперь она должна возвращать кроме курса дату, которая передаётся в ответе сервера.
# Дата должна быть в виде объекта date. Подумайте, как извлечь дату из ответа,
# какой тип данных лучше использовать в ответе функции?

import datetime

from requests import get, utils


def currency_rates(currency='USD'):
    """ Принимает str с названием валюты 3 символа, Возвращает кортеж вида (дата: datetime, курс_валюты: float)"""
    # если валюта не найдена - возвращает None
    currency = currency.upper() # возводим в вверхний регистр входную валюту
    value = None # на случай если валюту не найдем, будем возвращать None
    response = get(' http://www.cbr.ru/scripts/XML_daily.asp') #парсим сайт
    encodings = utils.get_encoding_from_headers(response.headers) #узнаем шифр
    content = response.content.decode(encoding=encodings) #берем расшифрованный контент
    splited_content = content.split('<CharCode>') #разбиваем строку на список
    data = splited_content[0].split('Date="')[1][:10] #вытаскиваем дату из первой строки
    year = int(data[6:10])
    month = int(data[3:5]) #разбиваем дату на год месяц и день
    day = int(data[0:2])
    data_in_datetime = datetime.date(year=year, month=month, day=day) #сохраняем в формате даты
    for element in splited_content: #перебираем список в поиске требуемой валюты
        if element[:3] == currency: # нашли строчку с требуемой валютой
            splited_data = element.split('<Value>')
            value = float(splited_data[1][:16].rstrip('</Value>').replace(',','.')) #флоат, убираем мусор справа
    return data_in_datetime, value


result_usd = currency_rates('usd')
print(f"Курс USD на дату {result_usd[0]} равен {result_usd[1]} рублей")

result_usd = currency_rates('EUR')
print(f"Курс EUR на дату {result_usd[0]} равен {result_usd[1]} рублей")

