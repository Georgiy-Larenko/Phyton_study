import os
import time


# Функция для обновления заметки

def update_note():
    note_id = input("Введите идентификатор заметки: ")
    filename = f"Intermediate_work\data\{note_id}.json"
    if os.path.exists(filename):
        note_title = input("Введите новый заголовок заметки: ")
        note_body = input("Введите новое тело заметки: ")
        note_date = time.strftime('%Y-%m-%d %H:%M:%S')
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"Заголовок: {note_title}\n")
            f.write(f"Дата создания: {note_date}\n")
            f.write(f"Дата последнего изменения: {note_date}\n")
            f.write(f"Тело заметки:\n{note_body}")
        print("Заметка обновлена успешно!")
        
    else:
        print("Заметка не найдена.")
        