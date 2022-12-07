# 2. Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все
# конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"


from random import randint


player1 = input("Введите имя первого игрока: ")
player2 = "Bot"
value = 2021


# Считаем очередность


flag = randint(0, 2)                         

if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")


# Запрашиваем количество конфет


def input_data(name):
    x = int(input(f"{name}, сколько возьмете конфет: "))

    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет (от 1 до 28): "))
    return x


# Расчеты бота


def bot_calculate(value):
    k = randint(1,29)
    while value - k <= 28 and value > 29:
        k = randint(1,29)
    return k


# Считаем кто сколько взял и остаток


def attention(name, k, counter, value):
    print('')
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось {value} конфет.")
    print('')


count_pl1 = 0 
count_bot = 0


while value > 28:

    if flag:
        k = input_data(player1)
        count_pl1 += k
        value -= k
        flag = False
        attention(player1, k, count_pl1, value)
        
    else:
        k = bot_calculate(value)
        count_bot += k
        value -= k
        flag = True
        attention(player2, k, count_bot, value)

if flag:
    print(f"{player1} выиграл ")
else:
    print(f"{player2} выиграл ")