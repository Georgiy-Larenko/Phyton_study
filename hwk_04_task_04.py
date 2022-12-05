# Задача 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# *Пример:*

# - k = 2   =>   2*x² + 4*x + 5 = 0  или  x² + 5 = 0 или  10*x² = 0

import random

k1 = int(input("Введите натуральную степень k: "))
k2 = int(input("Введите натуральную степень k: "))


def create_mn(k):
    lst = []
    for i in range (k + 1):
        lst.append(random.randint(0,101))
    return lst


def create_str(koef):
    lst = koef[::-1]
    str = ''

    if len(lst) < 1:
        str = 'x = 0'

    else:
        for i in range(len(lst)):

            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                str += f'{lst[i]}x^{len(lst)-i-1}'

                if lst[i+1] != 0:
                    str += ' + '

            elif i == len(lst) - 2 and lst[i] != 0:
                str += f'{lst[i]}x'

                if lst[i+1] != 0:
                    str += ' + '

            elif i == len(lst) - 1 and lst[i] != 0:
                str += f'{lst[i]} = 0'

            elif i == len(lst) - 1 and lst[i] == 0:
                str += ' = 0'

    return str




file = open('Homework\hwk_04_task_04_result_list_1', 'w')
koef1 = create_mn(k1)
file.write(create_str(koef1))
file.close()

file = open('Homework\hwk_04_task_04_result_list_2', 'w')
koef2 = create_mn(k2)
file.write(create_str(koef2))
file.close()