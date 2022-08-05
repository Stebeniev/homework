#Вспоминаем работу с файлом. Есть файл, в котором много англоязычных текстовых строк.
#Считаем частоту встретившихся слов в файле, но через функции и map, без единого цикла!
import sys


def fun(elem):
    if elem in my_dict:
        my_dict[elem] += 1
    else:
        my_dict[elem] = 1
    return elem


filename = sys.argv[1]
f = open(filename, 'r')
s = f.read()
new_list = s.split()
my_dict = {}

res = list(map(fun, new_list))
print(res)
print(my_dict)
