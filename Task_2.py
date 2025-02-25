import pandas as pd  # импортируем библиотеку pandas для работы с данными
import matplotlib.pyplot as plt  # импортируем библиотеку matplotlib для построения графиков

# загружаем данные из Excel файла 'student.xlsx' в DataFrame
df = pd.read_excel('student.xlsx')

# проверяем, какие столбцы есть в DataFrame
print(df.columns)

# создаем столбчатую диаграмму
plt.figure(figsize=(10, 6))  # задаем размер графика
plt.bar(df['Имя'], df['Оценка'], color='skyblue')  # строим столбчатую диаграмму

# добавляем заголовок и подписи к осям
plt.title('Оценки студентов', fontsize=16)  # заголовок графика
plt.xlabel('Имя студента', fontsize=14)  # подпись оси X
plt.ylabel('Оценка', fontsize=14)  # подпись оси Y

# поворачиваем подписи на оси X для лучшей читаемости
plt.xticks(rotation=45)

# отображаем график
plt.tight_layout()  # автоматически подгоняем элементы графика
plt.show()  # показываем график