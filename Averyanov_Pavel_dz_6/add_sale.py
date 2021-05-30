import sys
total_arguments = len(sys.argv[1:]) #всего параметров передано через терминал
if total_arguments == 1: #ожидаем только 1 параметр
    with open('bakery.csv', 'a', encoding='utf-8') as file_1:
        file_1.write(str(sys.argv[1])+'\n')
else:
    print('параметры не заданы')
