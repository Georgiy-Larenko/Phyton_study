from import_dt import import_dt
from export_dt import export_dt
from print_dt import print_dt
from search_dt import search_dt



def input_data():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    phone_number = input("Введите телефон: ")
    note = input("Введите примечание: ")
    return [last_name, first_name, phone_number, note]


def choice_todo():
    print("Какое действие выполняем?:\n\
    1 - Импорт данных;\n\
    2 - Экспорт данных;\n\
    3 - Поиск контакта;\n\
    4 - Завершение работы.")

    choice = input("Введите цифру: ")
    flag = True

    while flag == True:

        if choice == '1':
            flag == True
            sep = ';'
            import_dt(input_data(), sep)
            print("-" * 20)

            choice = input("Что делаем дальше?: ")
    
        elif choice == '2':
            flag == True
            data = export_dt()
            print_dt(data)
            print("-" * 20)

            choice = input("Что делаем дальше?: ")

        elif choice == '3':
            flag == True
            word = input("Введите данные для поиска: ")
            data = export_dt() 
            item = search_dt(word, data)

            if item != None:
                print("Фамилия", "Имя", "Телефон", "Примечание")
                print("-" * 50)
                print(item[0], item[1], item[2], item[3])
                print("-" * 20)

                choice = input("Что делаем дальше?: ")

            else:
                print("Данные не обнаружены")
                print("-" * 20)

                choice = input("Что делаем дальше?: ")
        else:
            flag == False
            print("Работа завершена.")
            break