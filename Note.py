import json
import os
from datetime import datetime

class Note:
    def __init__(self, id, title, body):
        self.id = id
        self.title = title
        self.body = body
        self.timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

class NoteManager:
    def __init__(self, file_name):
        self.file_name = file_name
        if not os.path.exists(file_name):
            with open(file_name, 'w') as file:
                json.dump([], file)

    def get_notes(self):
        with open(self.file_name, 'r') as file:
            notes = json.load(file)
        return notes

    def save_notes(self, notes):
        with open(self.file_name, 'w') as file:
            json.dump(notes, file, default=lambda o: o.__dict__)

    def add_note(self, note):
        notes = self.get_notes()
        notes.append(note.__dict__)
        self.save_notes(notes)

    def edit_note(self, id, title, body):
        notes = self.get_notes()
        for note in notes:
            if note['id'] == id:
                note['title'] = title
                note['body'] = body
                note['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.save_notes(notes)

    def delete_note(self, id):
        notes = self.get_notes()
        notes = [note for note in notes if note['id'] != id]
        self.save_notes(notes)

if __name__ == "__main__":
    note_manager = NoteManager('notes.json')

    while True:
        print("\nВыберите действие:")
        print("1. Создать заметку")
        print("2. Показать заметки")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")

        choice = input("> ")

        if choice == '1':
            id = len(note_manager.get_notes()) + 1
            title = input("Введите заголовок заметки: ")
            body = input("Введите текст заметки: ")
            note = Note(id, title, body)
            note_manager.add_note(note)
            print("Заметка создана")
        elif choice == '2':
            notes = note_manager.get_notes()
            for note in notes:
                print(f"{note['id']}. {note['timestamp']} - {note['title']}: {note['body']}")
        elif choice == '3':
            id = int(input("Введите номер заметки для редактирования: "))
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новый текст заметки: ")
            note_manager.edit_note(id, title, body)
            print("Заметка отредактирована")
        elif choice == '4':
            id = int(input("Введите номер заметки для удаления: "))
            note_manager.delete_note(id)
            print("Заметка удалена")
        elif choice == '5':
            break
        else:
            print("Неверный выбор")