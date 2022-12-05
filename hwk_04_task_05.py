# Задача 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# Коэффициенты могут быть как положительными, так и отрицательными. Степени многочленов могут отличаться.

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
file.writelines(create_str(koef1))
file.close()

file = open('Homework\hwk_04_task_04_result_list_2', 'w')
koef2 = create_mn(k2)
file.writelines(create_str(koef2))
file.close()



# получение степени многочлена
def sqrt_mn(k):
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i+1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num


# получение коэффицента члена многочлена
def k_mn(k):
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num


# разбор многочлена и получение его коэффициентов
def calc_mn(st):

    st = st[0].replace(' ', '').split('=')
    st = st[0].split('+')
    lst = []
    l = len(st)
    k = 0

    if sqrt_mn(st[-1]) == -1:
        lst.append(int(st[-1]))
        l -= 1
        k = 1

    i = 1 # степень
    ii = l-1 # индекс

    while ii >= 0:

        if sqrt_mn(st[ii]) != -1 and sqrt_mn(st[ii]) == i:
            lst.append(k_mn(st[ii]))
            ii -= 1
            i += 1

        else:
            lst.append(0)
            i += 1
        
    return lst




file1 = open('Homework\hwk_04_task_04_result_list_1', 'r')
st1 = file1.readlines()
print(f"Первый многочлен {st1}")

file2 = open('Homework\hwk_04_task_04_result_list_2', 'r')
st2 = file2.readlines()
print(f"Второй многочлен {st2}")


lst1 = calc_mn(st1)
lst2 = calc_mn(st2)

lst_length = len(lst1)

if len(lst1) > len(lst2):
    lst_length = len(lst2)

result_lst = [lst1[i] + lst2[i] for i in range(lst_length)]
if len(lst1) > len(lst2):
    mm = len(lst1)
    for i in range(lst_length, mm):
        result_lst.append(lst1[i])
else:
    mm = len(lst2)
    for i in range(lst_length, mm):
        result_lst.append(lst2[i])


res_file = open('Homework\Hwk_04_task_05_result_list', 'w')
res_file.write(create_str(result_lst))
res_file.close()

res_file = open('Homework\Hwk_04_task_05_result_list', 'r')
st3 = res_file.readlines()
res_file.close()
print(f"Результирующий многочлен {st3}")