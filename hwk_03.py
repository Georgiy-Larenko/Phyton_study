# Задание 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

lst = [2, 3, 5, 9, 3]
result = 0

for i in range(len(lst)):
    if i % 2 != 0:
        result += lst[i]

print(f"Сумма элементов списка, стоящих на нечетных позициях: {result}")



# Задание 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

lst = [2, 3, 4, 5, 6]
lenght = len(lst)

def sum_lst(lst):

    if lenght % 2 != 0:
        l = lenght // 2 + 1
    else:
        lenght // 2

    for i in range(l):
        new_lst = lst[i] * lst[lenght - i - 1]
        print(new_lst, end = ' ')

sum_lst(lst)



# Задание 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


lst = [1.1, 1.2, 3.1, 5, 10.01]

new_lst = [round(i % 1, 2) for i in lst if i % 1 != 0]  # Пока i в списке при условии что остаток от деления элемента i не равен нулю, 
                                                        # то окугляем результат от деления до 2х знаков и заносим в новый список. 

print(max(new_lst) - min(new_lst))



# Задание 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10



num = int(input("Введите число: "))
s = " "

while num != 0:
    s = str(num % 2) + s
    num //= 2
print(s)



# Задание 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]



num = int(input("Input number: "))
fib1 = fib2 = nf1 = 1      # Значения для первых элементов списка Фибоначчи и негаФибоначчи
nf2 = (- 1)                # Значение второго элемента списка негаФибоначчи
lst = [fib1, fib2, ]       # Список Фибоначчи
nflst = [0, nf1, nf2, ]    # Список негаФибоначчи


for i in range(2, num):               # Составил список чисел Фибоначчи  
    fib1, fib2 = fib2, fib1 + fib2
    lst.append(fib2)

for i in range(2, num):               # Составил список чисел негаФибоначчи
    nf1, nf2 = nf2, nf1 - nf2
    nflst.append(nf2)

res_list = list(reversed(nflst))      # Создал третий список где положил развернутый список негаФибоначчи        
res_list = res_list + lst             # прибавил список Фибоначчи
print(res_list)