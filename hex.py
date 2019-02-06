#хэш

import hashlib

file = open('C:/Users/sales5/Desktop/testfile.txt', 'rb').read() #читаем файл (как бинарные данные)

h = hashlib.md5(file).hexdigest() #присваиваем переменной h хэш читаемого файла
print(h) #выводим хэш