# 5* Дан список чисел. Найдите все возрастающие последовательности. Порядок элементов менять нельзя.

# *Пример:* 

# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.


# var 1.


# lst = [1, 5, 2, 3, 4, 6, 1, 7]

# def ups(lst):
#     result = [lst[0]]
#     for i in lst:
#         if i > max(result):
#             result.append(i)
#     return result
    
# print(ups(lst))


# var 2.

num = (int(input("Input start index: ")))

lst = [1, 5, 2, 3, 4, 6, 1, 7]

res = [lst[num - 1]]
res = [i for i in range(len(lst)) if i > max(res)]
res.insert(0, lst[num - 1])

print(res)