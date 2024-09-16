'''Pandas: Обеспечивает мощные инструменты для анализа данных.'''
import pandas as pd

# Чтение данных из CSV файла
data = pd.read_csv('data.csv')

# Выводим первые 5 строк
print("Первые 5 строк данных:")
print(data.head())

# Простая статистика
print("Статистические данные:")
print(data.describe())

# Группировка по дате и вычисление средней величины
average_value = data['value'].mean()
print("Среднее значение:", average_value)

'''Matplotlib: Это инструмент для визуализации данных. 
С его помощью можно создавать разнообразные графики.'''
import matplotlib.pyplot as plt

# Визуализация данных
plt.figure(figsize=(10, 5))
plt.plot(data['date'], data['value'], marker='o')
plt.title('Значение по датам')
plt.xlabel('Дата')
plt.ylabel('Значение')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()  # Показываем график