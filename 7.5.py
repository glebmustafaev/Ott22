import  os
import time
from os import walk
from os.path import join, getmtime, getsize, dirname
from time import strftime, localtime
for root, dirs, files in os.walk(r'D:\Project Python\pythonProject\second'):
    for file in files:
        filepath = join(file)
        filetime = getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = getsize(filepath)
        parent_dir = dirname(filepath)
        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
