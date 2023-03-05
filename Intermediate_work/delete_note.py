import os


# Функция для удаления заметки
def delete_note():
    note_id = input("Введите идентификатор заметки: ")
    filename = f"Intermediate_work\data\{note_id}.json"
    if os.path.exists(filename):
        os.remove(filename)
        print("Заметка удалена успешно!")
        
    else:
        print("Заметка не найдена.")
        