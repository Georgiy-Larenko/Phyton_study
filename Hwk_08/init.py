from read_data import read_data


def init():
    if not (len(read_data()) > 0):
        
        with open("Homework\Hwk_08\data\Persons.csv", 'a+') as file:
            file.write("id;surname;name;class;status\n")

        with open("Homework\Hwk_08\data\Adress.csv", 'a+') as file:
            file.write("id;city;street;house;apartament;other\n")

        with open("Homework\Hwk_08\data\Class.csv", 'a+') as file:
            file.write("id;row;col\n")