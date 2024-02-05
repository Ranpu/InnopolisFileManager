import sqlite3
import tkinter as tk
from tkinter import ttk


class Database:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.create_table()

    # Метод для создания базы данных и таблицы, если они не существуют
    def create_table(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS people (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    age INTEGER NOT NULL
                )
            """
            )
            self.conn.commit()
        except Exception as e:
            print(f"Error creating table: {e}")

    # Метод для заполнения базы данных из массива словарей
    def insert_data(self, data):
        if isinstance(data, list):
            for elem in data:
                self._insert_data(elem)
        else:
            self._insert_data(data)

    def _insert_data(self, elem):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                """
                INSERT INTO people (first_name, last_name, age)
                VALUES (?, ?, ?)
            """,
                (elem["first_name"], elem["last_name"], elem["age"]),
            )
            self.conn.commit()
        except Exception as e:
            print(f"Error inserting data: {e}")

    # Метод для получения данных из базы данных и вывода их в список
    def fetch_data(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT first_name, last_name, age FROM people")
            return cursor.fetchall()
        except Exception as e:
            print(f"Error fetching data: {e}")

    # Проверка заполненности базы
    def check_fullness(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM people")
        count = cursor.fetchone()[0]
        return bool(count)


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("People Database App")

        self.db = Database("people.db")

        self.create_widgets()

    def create_widgets(self):
        # Задаем основу таблицы
        columns = ("First Name", "Last Name", "Age")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        self.tree.pack(pady=10)

        # Заполняем таблицу
        data = self.db.fetch_data()
        for row in data:
            self.tree.insert("", "end", values=row)

        # Кнопка выхода
        exit_button = tk.Button(self.root, text="Exit", command=self.root.destroy)
        exit_button.pack()


# Массив со словарями для первичного заполнения
initial_data = [
    {"first_name": "John", "last_name": "Doe", "age": 25},
    {"first_name": "Jane", "last_name": "Smith", "age": 30},
    {"first_name": "Bob", "last_name": "Johnson", "age": 22},
    {"first_name": "John", "last_name": "Johnson", "age": 22},
]

# Инициализируем БД
db = Database("people.db")

# Заполняем БД если она пустая
if not db.check_fullness():
    db.insert_data(initial_data)

# Инициализируем и запускаем приложение
root = tk.Tk()
app = App(root)
root.mainloop()
