import os
import time

from create_note import create_note
from view_note import view_note
from update_note import update_note
from delete_note import delete_note




def choice_todo():
    print("Выберите действие:")
    print("1. Создать новую заметку")
    print("2. Просмотреть заметку")
    print("3. Обновить заметку")
    print("4. Удалить заметку")
    print("0. Выйти из программы")
    choice = input("Введите номер действия: ")

    while True:
        if choice == '1':
            create_note()
            choice = input("Что делаем дальше?: ")
        elif choice == '2':
            view_note()
            choice = input("Что делаем дальше?: ")
        elif choice == '3':
            update_note()
            choice = input("Что делаем дальше?: ")
        elif choice == '4':
            delete_note()
            choice = input("Что делаем дальше?: ")
        elif choice == '0':
            print("Программа завершена.")
            break
        else:
            print("Некорректный ввод.")

    