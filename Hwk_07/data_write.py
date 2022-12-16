

def input_data():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    phone_number = input("Введите телефон: ")
    note = input("Введите примечание: ")
    return [last_name, first_name, phone_number, note]


def write_scv(item):
    file = 'Phonebook.csv'
    with open(file, 'a', encoding = 'utf-8') as data:
        data.write(f'{item[0]};{item[1]};{item[2]};{item[3]}\n')


def write_txt(item):
    file = 'Phonebook.txt'
    with open(file, 'a', encoding = 'utf-8') as data:
        data.write(
            f'Фамилия: {item[0]}\n\nИмя: {item[1]}\n\nНомер телефона: {item[2]}\n\nОписание: {item[3]}\n\n\n')