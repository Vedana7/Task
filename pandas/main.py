import pandas as pd

df_excel = pd.read_excel('academic_performance_student (1).xlsx')

while True:
    print("Что вы хотите сделать?")
    print("1. вввывести весь дата сэт")
    print("2. вывести конкретную строчку из датасэта")
    print("3. вывести столбец")
    print("4. вывести ячейку")
    print("5. выход")

    n = int(input("введите номер действия: "))

    if n == 1:
        print(df_excel)

    elif n == 2:
        index = int(input("Введите индекс строки: "))
        if 0 <= index < len(df_excel):
            print(df_excel.iloc[index])
        else:
            print("Индекс вне диапазона")

    elif n == 3:
        col_index = int(input("Введите индекс столбца: "))
        if 0 <= col_index < df_excel.shape[1]:
            print(df_excel.iloc[:, col_index])
        else:
            print("Индекс вне диапазона")


    elif n == 5:
             print("Выход из программы")
    break

else:
        print("неверный номер действия")





