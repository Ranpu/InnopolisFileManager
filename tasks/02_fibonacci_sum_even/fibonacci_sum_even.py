def fibonacci_sum_even(n):
    fib_sequence = [0, 1]
    even_sum = 0
    while len(fib_sequence) <= n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    for num in fib_sequence:
        if num % 2 == 0:
            even_sum += num
    return even_sum


def alt_fibonacci_sum_even(n):
    a, b = 0, 1
    even_sum = 0
    count = 0
    if n <= 2:
        return 0
    n -= 2
    while count <= n:
        a, b = b, a + b
        print(a, b)
        even_sum = even_sum + b if b % 2 == 0 else even_sum
        print(even_sum)
        count += 1
    return even_sum


if __name__ == "__main__":
    while True:
        value = input(
            "Введите целое неотрицательное число больше нуля или exit для выходы: "
        )
        if value == "exit":
            break
        try:
            value = float(value)
        except ValueError:
            print("Значение должно быть числом.")
            continue
        if value <= 0:
            print("Число должно быть больше нуля.")
            continue
        if value != int(value):
            print("Число должно быть целым.")
            continue
        result = fibonacci_sum_even(value)
        print(
            "Сумма всех четных чисел последовательности Фибоначчи"
            f"до {int(value)}-го элемента равна {result}."
        )
