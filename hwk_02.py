###### Задание 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0.56 -> 11

# num = str(input('Введите число: '))
# sum = 0

# for i in str(num):
#     if i != ".":
#         sum += int(i)
# print(f"Сумма цифр числа {num} равна {sum}")



###### Задание 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1 * 2, 1 * 2 * 3, 1 * 2 * 3 * 4)
# Запрещено использовать функцию factorial из библиотеки math


# n = int(input("Введите число: "))
# lst = []
# sum = 0


# def mult(n):
#     if n == 1:
#         return n
#     else:
#         return n * mult(n - 1)


# for n in range(1, n + 1):
#     lst.append(mult(n))

# print(f"Произведения чисел от 1 до {n}:  {lst}")



###### Задание 3. Задайте список из n чисел последовательности (1 + 1 / n)**n и выведите на экран их сумму.

# *Пример:*

# - Для n = 6: [2.0, 2.25, 2.37, 2.44, 2.488, 2.52]    ->    14.072    (Округлять не обязательно)

# n = int(input('Введите число: '))
# lst = []

# for i in range(1, n + 1):
#     result = round((1 + 1/ i) ** i, 3)
#     lst.append(result)


# print(f'Последовательность: {lst}')
# print(f'Сумма: {round(sum(lst), 3)}')



###### Задание 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.

# n = int(input('Задайте длину списка: '))
# lst = []

# for i in range(-n , n + 1):
#     lst.append(i)
# print(lst)

# a = int(input('Введите позицию А: '))
# b = int(input('Введите позицию B: '))

# mult = lst[a-1] * lst[b-1]

# print(f'Позиция А: {lst[a-1]} \nПозиция B: {lst[b-1]} \nПроизведение позиций: {mult}')



# ##### Задание 5. Реализуйте алгоритм перемешивания списка.
# Из библиотеки random использовать можно только randint

# from random import randint


# def mix_lst(lst):
#     for i in range(len(lst)):
#         new_i = randint(0, len(lst) - 1)
#         lst[i], lst[new_i] = lst[new_i], lst[i]


# lst_ = [1, 2, 3, 4 ,5 ,6 ,7 ,8 ,9 ,0]

# print(f'Начальный массив: {lst_}')   
# mix_lst(lst_)
# print(f'Перемешанный массив: {lst_}')
