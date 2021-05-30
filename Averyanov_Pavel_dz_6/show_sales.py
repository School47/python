import sys
import itertools
total_arguments = len(sys.argv[1:]) #всего параметров передано через терминал
if total_arguments == 0: #Параметров нет, выводим весь файл
    with open('bakery.csv', 'r', encoding='utf-8') as file_1:
        for line in file_1:
            print(line.rstrip('\n'))
elif total_arguments == 1: # 1 параметр - выводить все записи с номера, равного этому числу, до конца;
    with open('bakery.csv', 'r', encoding='utf-8') as file_1:
        lines = itertools.islice(file_1, int(sys.argv[1]), None)
        for line in lines:
            print(line.rstrip('\n'))
elif total_arguments == 2: #выводить записи c первого по второй номер включительно
    with open('bakery.csv', 'r', encoding='utf-8') as file_1:
        lines = itertools.islice(file_1, int(sys.argv[1])-1, int(sys.argv[2]))
        for line in lines:
            print(line.rstrip('\n'))

else:
    print('Слишком много параметров!')
