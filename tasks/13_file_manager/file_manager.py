import os
import shutil


def create_file(file_name):
    try:
        with open(file_name, "w"):
            print(f"Файл '{file_name}' успешно создан.")
    except Exception as e:
        print(f"Ошибка при создании файла '{file_name}': {e}")


def create_folder(folder_name):
    try:
        os.makedirs(folder_name)
        print(f"Папка '{folder_name}' успешно создана.")
    except Exception as e:
        print(f"Ошибка при создании папки '{folder_name}': {e}")


def delete_file(file_name):
    try:
        os.remove(file_name)
        print(f"Файл '{file_name}' успешно удален.")
    except Exception as e:
        print(f"Ошибка при удалении файла '{file_name}': {e}")


def delete_folder(folder_name):
    try:
        shutil.rmtree(folder_name)
        print(f"Папка '{folder_name}' успешно удалена.")
    except Exception as e:
        print(f"Ошибка при удалении папки '{folder_name}': {e}")


def move_file(source, destination):
    try:
        shutil.move(source, destination)
        print(f"Файл '{source}' успешно перемещен в '{destination}'.")
    except Exception as e:
        print(f"Ошибка при перемещении файла '{source}': {e}")


def copy_file(source, destination):
    try:
        shutil.copy2(source, destination)
        print(f"Файл '{source}' успешно скопирован в '{destination}'.")
    except Exception as e:
        print(f"Ошибка при копировании файла '{source}': {e}")


if __name__ == "__main__":
    while True:
        print("\n1. Создать файл")
        print("2. Создать папку")
        print("3. Удалить файл")
        print("4. Удалить папку")
        print("5. Переместить файл")
        print("6. Скопировать файл")
        print("7. Выйти")

        choice = input("Выберите действие (1-7): ")

        if choice == "1":
            file_name = input("Введите имя файла: ")
            create_file(file_name)
        elif choice == "2":
            folder_name = input("Введите имя папки: ")
            create_folder(folder_name)
        elif choice == "3":
            file_name = input("Введите имя файла для удаления: ")
            delete_file(file_name)
        elif choice == "4":
            folder_name = input("Введите имя папки для удаления: ")
            delete_folder(folder_name)
        elif choice == "5":
            source = input("Введите имя файла для перемещения: ")
            destination = input("Введите путь назначения: ")
            move_file(source, destination)
        elif choice == "6":
            source = input("Введите имя файла для копирования: ")
            destination = input("Введите путь назначения: ")
            copy_file(source, destination)
        elif choice == "7":
            print("Программа завершена.")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите от 1 до 7.")
