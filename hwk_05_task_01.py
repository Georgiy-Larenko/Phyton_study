# 1 Напишите программу, удаляющую из файла все слова, содержащие "абв".
# ываабв лповап абвцукв алоабвабв ываываыв

text = input('Введите текст через пробел: ')
print(f'Введенный текст: {text}')

find = 'абв'
result = [i for i in text.split() if find not in i]
print(f'Результат без слов, содержащих "абв": {" ".join(result)}')