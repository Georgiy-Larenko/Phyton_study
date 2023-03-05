import os

# Функция для просмотра заметки

def view_note():
    note_id = input("Введите идентификатор заметки: ")
    filename = f"Intermediate_work\data\{note_id}.json"
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        print(content)
        
    else:
        print("Заметка не найдена.")
        