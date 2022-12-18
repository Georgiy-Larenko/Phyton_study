

def import_dt(data, sep=None):

    with open('Homework\Hwk_07\Phonebook.csv', 'a+', encoding='utf-8') as file:
        if sep == None:
            for i in data:
                file.write(f"{i}\n")
            file.write(f"\n")
        else:
            file.write(sep.join(data))
            file.write(f"\n")