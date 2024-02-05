import os
from datetime import datetime
from pathlib import PurePath

import cv2
import numpy as np


class OpenCVIMGProc:
    def __init__(self):
        self.images = []
        self.names = []

    def load_image(self):
        try:
            file_path = input("Введите путь к файлу изображения: ")
            file_name = PurePath(file_path).parts[-1]
            image = cv2.imread(file_path)
            if image is None:
                raise Exception(
                    "Не удалось загрузить изображение. Проверьте путь к файлу."
                )
            self.names.append(file_name)
            self.images.append(image)
        except Exception as e:
            print(f"Ошибка: {e}")
        finally:
            return None

    def save_image(self):
        try:
            file_path = input("Введите путь для сохранения файла: ")
            current_datetime = datetime.now().strftime("%d.%m-%H.%M")
            for index in range(len(self.images)):
                file_extension = os.path.splitext(self.names[index])[1]
                save_path = os.path.join(
                    file_path, f"{self.names[index]}-{current_datetime}{file_extension}"
                )
                cv2.imwrite(save_path, self.images[index])
                print(f"Изображение успешно сохранено по пути: {save_path}")
        except Exception as e:
            print(f"Ошибка при сохранении изображения: {e}")
        finally:
            return None

    def crop_image(self):
        try:
            x = int(input("Введите начальную координату X для обрезки: "))
            y = int(input("Введите начальную координату Y для обрезки: "))
            w = int(input("Введите ширину для обрезки: "))
            h = int(input("Введите высоту для обрезки: "))
            for index in range(len(self.images)):
                self.images[index] = self.images[index][y : y + h, x : x + w]
        except Exception as e:
            print(f"Ошибка при обрезке изображения: {e}")
        finally:
            return None

    def rotate_image(self):
        try:
            angle = float(input("Введите угол поворота (в градусах): "))
            for index in range(len(self.images)):
                height, width = self.images[index].shape[:2]
                center = (width // 2, height // 2)
                rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
                self.images[index] = cv2.warpAffine(
                    self.images[index], rotation_matrix, (width, height)
                )
        except Exception as e:
            print(f"Ошибка при повороте изображения: {e}")
        finally:
            return None

    def mirror_image(self):
        try:
            axis = input(
                "Выберите ось отзеркаливания (h - горизонтально, v - вертикально): "
            ).lower()
            if axis == "h" or axis == "v":
                for index in range(len(self.images)):
                    if axis == "h":
                        self.images[index] = cv2.flip(self.images[index], 1)
                    else:
                        self.images[index] = cv2.flip(self.images[index], 0)
            else:
                print(
                    "Некорректный выбор оси. Используйте 'h' для"
                    "горизонтального или 'v' для вертикального отзеркаливания."
                )
        except Exception as e:
            print(f"Ошибка при отзеркаливании изображения: {e}")
        finally:
            return None

    def blur_image(self):
        try:
            kernel_size = int(
                input("Введите размер ядра для размытия (нечетное число): ")
            )
            if kernel_size % 2 == 0:
                raise ValueError("Размер ядра должен быть нечетным числом.")
            for index in range(len(self.images)):
                self.images[index] = cv2.GaussianBlur(
                    self.images[index], (kernel_size, kernel_size), 0
                )
        except Exception as e:
            print(f"Ошибка при применении размытия к изображению: {e}")
        finally:
            return None

    def sharpen_image(self):
        try:
            kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
            for index in range(len(self.images)):
                self.images[index] = cv2.filter2D(self.images[index], -1, kernel)
        except Exception as e:
            print(f"Ошибка при увеличении резкости изображения: {e}")
            return None


def main():
    ocv = OpenCVIMGProc()

    while True:
        print("\n1. Загрузить изображение")
        print("2. Обрезать изображение")
        print("3. Поворот изображения")
        print("4. Отзеркалить изображение")
        print("5. Размытие изображение")
        print("6. Увеличение резкости изображения")
        print("9. Сохранить изображение")
        print("0. Выйти из программы")

        choice = input("Выберите действие (введите номер): ")

        match choice:
            case "1":
                ocv.load_image()
            case "2":
                ocv.crop_image()
            case "3":
                ocv.rotate_image()
            case "4":
                ocv.mirror_image()
            case "5":
                ocv.blur_image()
            case "6":
                ocv.sharpen_image()
            case "9":
                ocv.save_image()
            case "0":
                print("Программа завершена.")
                break
            case _:
                print("Некорректный выбор. Пожалуйста, выберите существующий пункт.")


if __name__ == "__main__":
    main()
