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
