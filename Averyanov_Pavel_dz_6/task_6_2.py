# Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
# [
#     ...
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('173.255.199.22', 'GET', '/downloads/product_2'),
#     ...
# ]
#
# *(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
# Примечание: спамер — это клиент, отправивший больше всех запросов;
# код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

clients = {} # в словарь будем добавлять клиентов с ключем по ИП и значение - количество отправленных им запросов
ip_spammer = ''
number_of_requests = 0

with open('nginx_logs.sql', 'r', encoding='utf-8') as file_1:
   for line in file_1: #фаил читаем построчно, поэтому его размер может превышать ОЗУ ПК.
       ip = line.split(' - - [')[0] #парсим ИП
       if ip.replace('.','').isdigit(): #вроде похоже на ИП адресс
           if clients.get(ip) != None: # клиент уже есть в словаре
               clients[ip] += 1 #увеличиваем запись в словаре на количество запросов
               if number_of_requests < clients[ip]: # сравниваем текущего клиента со спамером
                   ip_spammer = ip # теперь текущий клиент - спамер
                   number_of_requests = clients[ip] # и это количество его запросов
           else:
               clients[ip] = 1 # клиента еще нет в словаре  - добавляем

# for key, value in clients.items():
#     print(key, value)

print(f'Ип спамера - {ip_spammer}, количество отправленных им запросов - {number_of_requests}')
