import os
import shutil

from fileinput import filename

from os.path import split
#
# number_str = "1a2a3a4a5"
# def get_sum_numbers(number_str):
#     a = set(number_str)
#     return a
#
#
#
# result = get_sum_numbers(number_str)
# print(result)




# функция open (file, mode, encoding) - открывает файл
# file - путь к файлу (абсолютный или относительно скрипта)
# mode - режим открытия файла
# encoding - кодировка
#
# основные режимы: r - чтение,  w - запись с пересозданием файла, a - добавление в коенц файла

# mode='w' - открытие файла в режиме создания нового файла или перезаписи существующего
myfile = open(file='myfile.txt', mode='w', encoding='utf-8')
print(type(myfile))

# write - запись в файл
myfile.write('Python!\n')
text = "Forever!"
myfile.write(text)

# после завершения работы с файлом - закрываем его
# myfile.close()

# \t - символ табуляции
# \n - символ перевода на новую строку

my_list = ['alena', 'elena']

# for item in my_list:
#     myfile.write('\n'+item+'\n')

# names = '\n'.join(my_list)


for item in my_list:
     myfile.write(item.strip(',!')+'\n')

myfile.close()

# mode='а' - открытие файла в режиме добавления в конец файла
myfile = open(file='myfile.txt', mode='a', encoding='utf-8')
myfile.write('Python!\n')
myfile.writelines(my_list)

myfile.close()

# mode='r' - открытие файла для чтения
myfile = open(file='myfile.txt', mode='r', encoding='utf-8')
text_from_file = myfile.read()
text_rows = text_from_file.split('\n')
print(text_rows)

# myfile.seek(0) - пеермещает курсор в начало файла
myfile.seek(0)
text_lines = myfile.readline()
print(text_lines)

name = 'flex'
last_name = 'ivanov'
print(name, last_name, sep='---')
print(*my_list, sep='\n')


# with ... as - контестный менеджер
# with open(file='myfile.txt', mode='r', encoding='utf-8') as my_file:
#     text_from_f = my_file.read()

# проверка наличия файла

file_name = 'myfilenew.txt'
if os.path.exists(file_name):
    with open(file=file_name, mode='r', encoding='utf-8') as my_file:
        text_from_f = my_file.read()
else:
    with open(file=file_name, mode='w', encoding='utf-8') as my_file:
        pass

# rename file
filename_new = f'new_{file_name}'
if os.path.exists(file_name):
        os.rename(file_name, filename_new)
else:
    print(f'файл {filename_new} уже существует')

# remove file
if os.path.exists(filename_new):
    os.remove(filename_new)
    print(f'файл {filename_new} удалён')


dir_name = 'files'
if not os.path.exists(dir_name):
    os.makedirs(dir_name, exist_ok=True)

os.makedirs(dir_name, exist_ok=True)

# удаление каталога
# os.rmdir(dir_name)

with open(file=f'{dir_name}/{file_name}', mode='w', encoding='utf-8') as my_file:
    pass

# os.rmdir(dir_name)
shutil.rmtree(dir_name)