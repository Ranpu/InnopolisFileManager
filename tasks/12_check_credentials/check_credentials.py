import tkinter as tk
from tkinter import messagebox


def check_credentials():
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    if entered_username == "user" and entered_password == "passwd":
        messagebox.showinfo("Успех", "Вход выполнен успешно!")
    else:
        messagebox.showerror("Ошибка", "Неправильный логин или пароль.")


# Создаем главное окно
root = tk.Tk()
root.title("Авторизация")

# Создаем и размещаем виджеты на главном окне
tk.Label(root, text="Логин:").grid(row=0, column=0, padx=10, pady=10)
tk.Label(root, text="Пароль:").grid(row=1, column=0, padx=10, pady=10)

username_entry = tk.Entry(root)
password_entry = tk.Entry(root, show="*")

username_entry.grid(row=0, column=1, padx=10, pady=10)
password_entry.grid(row=1, column=1, padx=10, pady=10)

login_button = tk.Button(root, text="Войти", command=check_credentials)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

# Запускаем главный цикл программы
root.mainloop()
