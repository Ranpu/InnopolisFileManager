def calculator():
    print("Добро пожаловать в программу калькулятор!")
    username = input("Введите логин: ")
    password = input("Введите пароль: ")

    if username == "admin" and password == "admin":
        print("Вход выполнен успешно. Можете пользоваться калькулятором.")
        while True:
            print("Выберите операцию:")
            print("1. Сложение (a + b)")
            print("2. Вычитание (a - b)")
            print("3. Умножение (a * b)")
            print("4. Деление (a / b)")
            print("5. Выйти из программы")
            choice = input("Введите номер операции (1/2/3/4/5): ")

            if choice in ("1", "2", "3", "4"):
                try:
                    num1 = float(input("Введите первое число (a): "))
                    num2 = float(input("Введите второе число (b): "))
                except ValueError:
                    print("Введено значение отличное от числа.")
                    continue

                if choice == "1":
                    print(f"{num1} + {num2} = {num1 + num2}")
                elif choice == "2":
                    print(f"{num1} - {num2} = {num1 - num2}")
                elif choice == "3":
                    print(f"{num1} * {num2} = {num1 * num2}")
                elif choice == "4":
                    if num2 != 0:
                        print(f"{num1} / {num2} = {num1 / num2}")
                    else:
                        print("Деление на ноль недопустимо!")
            elif choice == "5":
                print("Программа завершена.")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

    else:
        print("Неверный логин или пароль. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    calculator()
