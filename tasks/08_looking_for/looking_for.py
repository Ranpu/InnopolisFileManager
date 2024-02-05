import matplotlib.pyplot as plt
import pandas as pd

# Шаг 1: Загрузить датасет
df = pd.read_csv("./googleplaystore.csv")

# Шаг 2: Вывести первые 10 строк датасета
print("Первые 10 строк датасета:")
print(df.head(10))

# Шаг 3: Вывести случайные 5 строк датасета
print("\nСлучайные 5 строк датасета:")
print(df.sample(5))

# Шаг 4: Вывести количество строк и столбцов
print(f"\nКоличество строк и столбцов: {df.shape}")

# Шаг 5: Вывести данные о количестве пропущенных значений
print("\nКоличество пропущенных значений:")
print(df.isnull().sum())

# Шаг 6: Отбросить строки с пропущенными значениями
df = df.dropna()
print("\nДатасет после удаления строк с пропущенными значениями:")
print(df.head())

# Шаг 7: Найти самый большой и самый маленький рейтинги, а также среднее значение рейтинга
max_rating = df["Rating"].max()
min_rating = df["Rating"].min()
mean_rating = df["Rating"].mean()
print(f"\nСамый большой рейтинг: {max_rating}")
print(f"Самый маленький рейтинг: {min_rating}")
print(f"Среднее значение рейтинга: {mean_rating}")

# Шаг 8: Вывести первые 10 приложений с рейтингом не ниже 4.9
high_rated_apps = df[df["Rating"] >= 4.9]
print("\nПервые 10 приложений с рейтингом не ниже 4.9:")
print(high_rated_apps.head(10))

# Шаг 9: Преобразовать столбец 'Installs' в числовой формат
df["Installs"] = df["Installs"].str.replace(",", "")  # Убираем запятые
df["Installs"] = df["Installs"].str.replace("+", "")  # Убираем знак +
df["Installs"] = pd.to_numeric(df["Installs"], errors="coerce")

# Шаг 10: Вывести 5 самых часто скачиваемых приложений
top_downloaded_apps = df.nlargest(5, "Installs")
print("\n5 самых часто скачиваемых приложений:")
print(top_downloaded_apps)

# Шаг 11: Отрисовать график количества приложений для каждой категории
category_counts = df["Category"].value_counts()
category_counts.plot(
    kind="bar", figsize=(12, 6), title="Количество приложений по категориям"
)
plt.xlabel("Категория")
plt.ylabel("Количество приложений")
plt.savefig("./output.png")
plt.show()
