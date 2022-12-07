# 4 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.

# aaaasssdddwwwwwwwwwwwweeeffffff ->  4a3s3d9w3w3e6f 
# 4a3s3d9w3w3e6f-> aaaasssdddwwwwwwwwwwwweeeffffff


with open('Homework\hwk_05_task_04_RLE_1') as data:
    cod_text = data.read()


# Coding


def coding(text):
    count = 1
    res = ''
    for i in range(len(text) - 1):
        if text[i] == text[i + 1]:
            count += 1
        else:
            res = res + str(count) + text[i]
            count = 1
    if count > 1 or (text[len(text) - 2] != text[ - 1]):
        res = res + str(count) + text[ - 1]
    return res


print(f"Текст после кодировки: {coding(cod_text)}")


# DeCoding


with open('Homework\hwk_05_task_04_RLE_2') as data:
    decod_txt = data.read()


def decoding(text:str):
    count = ''
    str_decode = ''

    for char in text:
        if char.isdigit():
            count += char 
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode


print(f"Текст после декодирования: {decoding(decod_txt)}")