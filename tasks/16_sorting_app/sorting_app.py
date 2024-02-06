import threading
import time
import tkinter as tk
from tkinter import ttk


class SortingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting App")

        # Поле ввода текста
        self.input_label = tk.Label(root, text="Введите числа через запятую:")
        self.input_entry = tk.Entry(root)
        self.input_label.pack()
        self.input_entry.pack()

        # Раскрывающийся список для выбора сортировки
        self.sort_options = [
            "Сортировка пузырьком",
            "Сортировка выбором",
            "Сортировка вставками",
        ]
        self.sort_var = tk.StringVar(root)
        self.sort_var.set(self.sort_options[0])
        self.sort_label = tk.Label(root, text="Выберите метод сортировки:")
        self.sort_dropdown = ttk.Combobox(
            root, textvariable=self.sort_var, values=self.sort_options
        )
        self.sort_label.pack()
        self.sort_dropdown.pack()

        # Кнопка и поле вывода
        self.start_button = tk.Button(root, text="Start", command=self.start_sorting)
        self.output_label = tk.Label(root, text="Результат:")
        self.output_text = tk.Text(root, height=5, width=40, state=tk.DISABLED)

        self.start_button.pack()
        self.output_label.pack()
        self.output_text.pack()

    def start_sorting(self):
        # Получение введенной последовательности чисел
        input_sequence = self.input_entry.get()

        try:
            # Преобразование введенной строки в список чисел
            numbers = [int(num.strip()) for num in input_sequence.split(",")]
        except ValueError:
            self.output_text.config(state=tk.NORMAL)
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, "Ошибка: Введите корректные числа.")
            self.output_text.config(state=tk.DISABLED)
            return

        # Выбор метода сортировки
        selected_sort = self.sort_var.get()
        if selected_sort == "Сортировка пузырьком":
            sort_function = self.bubble_sort
        elif selected_sort == "Сортировка выбором":
            sort_function = self.selection_sort
        elif selected_sort == "Сортировка вставками":
            sort_function = self.insertion_sort
        else:
            self.output_text.config(state=tk.NORMAL)
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, "Ошибка: Неверный метод сортировки.")
            self.output_text.config(state=tk.DISABLED)
            return

        # Запуск сортировки в отдельном потоке для избежания блокировки GUI
        threading.Thread(
            target=self.perform_sorting, args=(numbers, sort_function)
        ).start()

    def perform_sorting(self, numbers, sort_function):
        start_time = time.time()
        sorted_numbers = sort_function(numbers)
        end_time = time.time()

        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(
            tk.END, f"Отсортированная последовательность: {sorted_numbers}\n"
        )
        self.output_text.insert(
            tk.END,
            f"Время затраченное на сортировку: {end_time - start_time:.6f} секунд",
        )
        self.output_text.config(state=tk.DISABLED)

    def bubble_sort(self, arr):
        n = len(arr)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def selection_sort(self, arr):
        n = len(arr)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr

    def insertion_sort(self, arr):
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr


if __name__ == "__main__":
    root = tk.Tk()
    app = SortingApp(root)
    root.mainloop()
