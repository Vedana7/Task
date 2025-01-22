import pandas as pd
df_excel = pd.read_excel('academic_performance_student.xlsx')
while True:
    print("Что вы хотите сделать? ")
    print("1.Вывести дата сэт")
    print("2.вывести конкретную (по индексу(пользователь вводит его)) строчку из датасэта")
    print("3.вывести столбец(пользователь вводит индекс) ")
    print("4.вывести ячейку (тоже можно поиск организовать через индекс )")
    n = int(input())
    if n == 1:
        print(df_excel.head(15))




