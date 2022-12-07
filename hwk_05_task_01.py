# 1 Напишите программу, удаляющую из файла все слова, содержащие "абв".
# ываабв лповап абвцукв алоабвабв ываываыв

text = input('Введите текст через пробел: ')
print(f'Введенный текст: {text}')

find = 'абв'
data = text.split()
result = [i for i in data if find not in i]
print(f'Результат без слов, содержащих "абв": {" ".join(result)}')


# var 2


def del_words(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

result_text = del_words(text)
print(f'Результат без слов, содержащих "абв": {result_text}')


# var 3

# text = "привет абв пока абвгд"                  # проверка без ввода
text = input('Введите текст через пробел: ')
res = " ".join(list(filter(lambda x: not "абв" in x, text.split())))
print(f'Результат без слов, содержащих "абв": {res}')
