
import time

# Функция для создания новой заметки
def create_note():
    note_id = input("Введите идентификатор заметки: ")
    note_title = input("Введите заголовок заметки: ")
    note_body = input("Введите тело заметки: ")
    note_date = time.strftime('%Y-%m-%d %H:%M:%S')

    # Создание файла заметки
    filename = f"Intermediate_work\data\{note_id}.json"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"Заголовок: {note_title}\n")
        f.write(f"Дата создания: {note_date}\n")
        f.write(f"Дата последнего изменения: {note_date}\n")
        f.write(f"Тело заметки:\n{note_body}")

    print("Заметка создана успешно!")
    
