class Calculator:
    def add(self, x, y):
        """Сложение двух чисел."""
        return x + y

    def subtract(self, x, y):
        """Вычитание одного числа из другого."""
        return x - y

    def multiply(self, x, y):
        """Умножение двух чисел."""
        return x * y

    def divide(self, x, y):
        """Деление одного числа на другое."""
        if y != 0:
            return x / y
        else:
            raise ValueError("Деление на ноль недопустимо")


if __name__ == "__main__":
    calculator = Calculator()

    while True:
        print("Выберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Выход")

        choice = input("Введите номер операции (1-5): ")

        if choice == "5":
            break

        if choice in ("1", "2", "3", "4"):
            x = float(input("Введите первое число: "))
            y = float(input("Введите второе число: "))

            if choice == "1":
                result = calculator.add(x, y)
            elif choice == "2":
                result = calculator.subtract(x, y)
            elif choice == "3":
                result = calculator.multiply(x, y)
            elif choice == "4":
                try:
                    result = calculator.divide(x, y)
                except ValueError as e:
                    print(f"Ошибка: {e}")
                    continue

            print(f"Результат: {result}")
        else:
            print("Неверный выбор. Пожалуйста, выберите от 1 до 5.")
