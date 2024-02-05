def binary_search(start, end, target):
    attempts = 0

    while start <= end:
        mid = (start + end) // 2
        attempts += 1

        if mid == target:
            return attempts
        elif mid < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1


if __name__ == "__main__":
    try:
        start_range = int(input("Введите начало диапазона: "))
        end_range = int(input("Введите конец диапазона: "))
        target_number = int(input("Введите искомое число: "))

        if start_range > end_range:
            print(
                "Ошибка: начало диапазона должно быть меньше или равно концу диапазона."
            )
        else:
            result = binary_search(start_range, end_range, target_number)

            if result != -1:
                print(f"Искомое число {target_number} найдено за {result} попыток.")
            else:
                print(
                    f"Искомое число {target_number} не найдено в указанном диапазоне."
                )
    except ValueError:
        print("Ошибка: введите корректные целочисленные значения.")
