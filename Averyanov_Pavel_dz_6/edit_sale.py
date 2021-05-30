# *(вместо 6) Добавить возможность редактирования данных при помощи отдельного скрипта:
# передаём ему номер записи и новое значение. При этом файл не должен читаться целиком — обязательное требование.
# Предусмотреть ситуацию, когда пользователь вводит номер записи, которой не существует.
import sys

num_string_to_edit = 11
new_record = 1
total_arguments = len(sys.argv[1:]) #всего параметров передано через терминал
if total_arguments == 2:#ожидаются параметры - номер записи и новое значение
    num_string_to_edit = int(sys.argv[1])
    new_record = int(sys.argv[2])
else:
    print('ожидаются параметры - номер записи и новое значение')
    exit()

total_number_of_strings = 0 #всего строк в файле в исходном файле.
with open('bakery.csv', 'r+', encoding='utf-8') as file_1:
    with open('temp_bakery.csv', 'w+', encoding='utf-8') as file_2:
        for line in file_1: #делаем построчно копию файла
            file_2.write(line)
            total_number_of_strings += 1
        file_2.seek(0) # копия сделала, возвращаем курсор и перезаписываем оригинальный файл с копии
        file_1.seek(0)
        if total_number_of_strings >= num_string_to_edit: # номер строки указан верно
            for line in range (1,total_number_of_strings+1):
                if line != num_string_to_edit:
                    file_1.write(file_2.readline())
                else:
                    file_1.write(str(new_record)+'\n') # нашли строку для изменения - добавляем новое значение.
                    file_2.readline() #также прочитываем строку в копии, чтобы курсор был в синхронной позиции
            file_1.truncate() #уничтожаем все что после курсора в исходном файле.
        else:
            print(f'Нельзя редактировать {num_string_to_edit} '
                  f'строку т.к. в файле всего {total_number_of_strings} строк с ценами!')