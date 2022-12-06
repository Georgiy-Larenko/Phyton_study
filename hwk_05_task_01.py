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