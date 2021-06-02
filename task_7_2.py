import yaml  # для чтения файла.
import os

with open('config.yaml') as file:
    file_tree = yaml.full_load(file) #загружаем в словарь данные из файла.


def unpack_tree(data):
    if type(data) == dict:  # словарь - ключ - это папка, значения - файлы или папки
        for key, val in data.items():
            print(f'Создаю папку: {key}')
            if not os.path.isdir(key):
                os.mkdir(key)
            os.chdir(key)
            unpack_tree(val)
            os.chdir('..')
    elif type(data) == list:
        for el in data:
            unpack_tree(el)
    elif type(data) == str:  # строка - это всегда файл.
        with open(data, 'w'):
            print(f'Создаю файл {data}')


unpack_tree(file_tree)
print('all done')
