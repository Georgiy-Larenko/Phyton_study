
# 3 Создайте программу для игры в "Крестики-нолики".

# Вариант интерфейса:


import emoji

board = list(range(1,10))


def draw_board(board):
    print(emoji.emojize(":minus:" * 7))
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print(emoji.emojize(":minus:" * 7))


def take_input(player_toker):
    valid = False
    while not valid:
        player_anwser = input("Куда поставим " + player_toker + "? ")

        try:
            player_anwser = int(player_anwser)    
        except:
            print("Некорректный ввод.")
            continue

        if player_anwser >= 1 and player_anwser <= 9:
            if(str(board[player_anwser - 1]) not in ':cross_mark:' and ':hollow_red_circle:'):
                board[player_anwser - 1] = player_toker
                valid = True
            else:
                print("Эта клетка уже занята")

        else:
            print("Введите число от 1 до 9.")


def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
        return False


def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0: 
            take_input(emoji.emojize(':cross_mark:'))
        else:
            take_input(emoji.emojize(':hollow_red_circle:'))
        counter += 1

        if counter > 3:
            tmp = check_win(board)
            if tmp:
                print("The winner is: " + tmp)
                win = True
                break

        if counter == 9:
            print(tmp, "Ничья!")
            break
    draw_board(board)
main(board)
