# Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
# а значения — общее количество файлов (в том числе и в подпапках),
# размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
#
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
import os
import collections


def show_me_some_statistic_baby(current_dir=os.getcwd()):
    print("current dir =", current_dir)
    stat_dict = collections.defaultdict(int)
    for path, dirs, files in os.walk(current_dir):
        for cur_file in files:
            rel_path = os.path.relpath(os.path.join(path, cur_file), current_dir)
            file_size = os.stat(rel_path).st_size
            # print(file_size)
            if file_size < 10:
                stat_dict[10] += 1
            elif file_size < 100:
                stat_dict[100] += 1
            elif file_size < 1000:
                stat_dict[1000] += 1
            elif file_size < 10000:
                stat_dict[10000] += 1
            elif file_size < 100000:
                stat_dict[100000] += 1
            elif file_size < 1000000:
                stat_dict[1000000] += 1
            else:
                stat_dict[10000000] += 1


    for key, value in sorted(stat_dict.items()):
        print(f'{key}:{value}')


some_folder = os.getcwd()
show_me_some_statistic_baby(some_folder)
