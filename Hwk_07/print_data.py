
def print_data(data):
    if len(data) > 0:
        print("Фамилия", "Имя", "Телефон", "Примечание")
        print("-"*85)
        for item in data:
            print(item[0], item[1], item[2], item[3])
    else:
        print("Справочник пуст!")