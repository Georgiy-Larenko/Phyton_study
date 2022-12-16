
from create_scv import create_data
from data_write import write_scv, write_txt, input_data
from export import export_data
from search_data import search_data


def view():
    print('-' * 50)
    print(export_data('Phonebook.txt'))
    print('-' * 50)
    print(export_data('Phonebook.csv'))


def record_data():
    info = input_data()
    write_scv(info)
    write_txt(info)


def choice():
    print("Что делаем?:\n\
    1 - Внести данные;\n\
    2 - Вывести данные;\n\
    3 - Поиск контакта.")
    choice = input("Введите цифру: ")

    if choice == '1':
        record_data()

    elif choice == '2':
        view()

    else:
        word = input("Введите данные для поиска: ")
        data = export_data()
        item = search_data(word, data)

        if item != None:
            print("Фамилия", "Имя", "Телефон", "Примечание")
            print(item[0], item[1], item[2], item[3])
        else:
            print("Данные не обнаружены")