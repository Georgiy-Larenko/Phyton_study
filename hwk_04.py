# Задача 1. Вычислить число π c заданной точностью d

# *Пример:*

# - при  d = 0.001, π = 3.141     10^{-1} ≤ d ≤10^{-10}

# from math import pi

# d = int(input("Введите точность числа π: "))
# x = 0
# count = 1

# for count in range (1, 100000):
#     x = x + 4 * ((-1) ** (count + 1)) / (2 * count - 1)
# print(round(x, d))


# # Для сравнения

# print(round(pi, d))



# Задача 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# *Пример*

# - при N = 236 ----> [2, 2, 59]

# n = int(input("input N: "))


# def mults(n):
#     lst = []
#     i = 2

#     while i * i <= n:
#         if n % i == 0:
#             lst.append(i)
#             n //= i
#         else:
#             i += 1
#     if n > 1:
#         lst.append(n)
#     return lst


# print(mults(n))




# Задача 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# *Пример*

# - при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]  ->   [2, 4, 5, 9]

lst = [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]


# def get_unique(lst):
#     res_lst  = []
#     for i in lst:
#         if lst.count(i) == 1:
#             res_lst.append(i)
#     return res_lst


# print(get_unique(lst))


# Var 2


# lst = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {lst}")

new_lst = []
[new_lst.append(i) for i in lst if i not in new_lst]

print(f"Список из неповторяющихся элементов: {new_lst}")
