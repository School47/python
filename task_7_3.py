# Создать структуру файлов и папок, как написано в задании 2
# (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#    |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
#
#
# Примечание: исходные файлы необходимо оставить;
# обратите внимание, что html-файлы расположены в родительских папках (они играют роль пространств имён);
# предусмотреть возможные исключительные ситуации;
# это реальная задача, которая решена, например, во фреймворке django.
import os
import shutil

project_name = 'my_project'
templates_folder = 'templates'
os.chdir(project_name)
templates_path = os.path.join(os.getcwd(), templates_folder)
print("templates path =", templates_path)
print("current dir =", os.getcwd())

for path, dirs, files in os.walk(os.getcwd()):
    for cur_dir in dirs:
        if cur_dir == templates_folder and os.path.join(path, cur_dir) != templates_path:
            print(f'папка {os.path.join(path, cur_dir)} -> будет скопирована в {templates_path}')
            shutil.copytree(os.path.join(path, cur_dir), templates_path, dirs_exist_ok=True)
