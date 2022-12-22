

def print_data(data, search = False):
    if len(data) > 0:
        print("id", "Фамилия", "Имя", "Класс", "Статус", "Ряд", "Парта", "Город", "Улица", "Дом", "Квартира", "Примечание")
        print()
        if not search:
            del data[0]
        for item in data:
            print(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11])
        print()
    else:
        print("Справочник пуст.")