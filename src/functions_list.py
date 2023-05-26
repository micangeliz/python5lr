import numpy as np


def print_table(df):
    print("\n2.1 вывод таблицы")
    print(df)


def print_table_first5(df):
    print("\n2.2 вывод первых 5 элементов таблицы")
    print(df.head())


def print_table_last5(df):
    print("\n2.3 вывод последних 5 элементов таблицы")
    print(df.iloc[-5:])


def describe(df):
    print("\n2.4 использовать функцию describe()")
    print(round(df["age"].describe()))


def find_cell(df):
    print(
        "\n2.5 считывание значения конкретной ячейки (с конкретным индексом из конкретной колонки) "
        "всеми известными вам способами")
    print("1 метод: " + df.iloc[0]['Mjob'])
    print("2 метод: " + df.at[0, 'Mjob'])
    print("3 метод: " + df['Mjob'].values[0])


def filter_str(df):
    print("\n2.6 фильтрация строк по диапазону индекса")
    print(df.filter(items=range(3, 9), axis=0))


def filter_set(df):
    print("\n2.7 фильтрация набора данных по какому-либо условию")
    print(df[df["age"] == 15])


def nan_add(df):
    print("\n2.8 работа с пропущенными значениями")
    df.iloc[5:7, 13] = np.nan  # генерация NaN
    print(df.iloc[5:7, 13])
    print("NaN значения:{}".format(df.isnull().values.any()))  # проверка наличия NaN
    for i in df.columns[df.isnull().any()]:  # восстановление NaN
        df[i].fillna(df[i].mean(), inplace=True)
    print(df.iloc[5:7, 13])
    print("NaN значения:{}".format(df.isnull().values.any()))  # проверка наличия NaN


def create_field(df):
    print("\n2.9. создание нового поля, вычисленного на основе значений других полей:")

    print("\n2.9.1 через выражение на базе имеющихся колонок")
    df["G_avg"] = (df["G1"] + df["G2"] + df["G3"]) / 3  # среднее значение оценок G
    print(round(df["G_avg"]))

    print("\n2.9.2 через DataFrame.apply")
    df["G_avg"] = df.apply(lambda G: (G.G1 + G.G2 + G.G3) / 3, axis=1)  # среднее значение оценок G
    print(round(df["G_avg"]))

    print("\n2.9.3 через Series.apply")
    df["G_avg"] = df["G_avg"].apply(lambda name: (name / 20) * 100)  # процентное соотношение среднего значения оценок G
    print(df["G_avg"])


def sorting(df):
    print("\n2.10 сортировка по какому-либо из полей")
    df.sort_values(by=["G_avg"], ignore_index=True, inplace=True,
                   ascending=False)  # по убыванию среднее значение оценок G
    print(df["G_avg"])


def statistics(df):
    print(
        "\n2.11 вычислить несколько статистик по колонкам (используйте встроенные агрегатные функции — любые на выбор)")
    print("\nСводная статистика для среднего значения оценок G среди учеников:")
    print(df["G_avg"].describe())
    print("\nКоличество учеников, у которых отец является опекуном:")
    counterFunc = df.apply(
        lambda x: True if x[10] == "father" else False, axis=1)
    numOfRows = len(counterFunc[counterFunc].index)
    print(numOfRows)


def value_counts(df):
    print("\n2.12 .value_counts()")
    print("mothers' works:{}".format(df["Mjob"].value_counts()))


def unique(df):
    print("\n2.13 Вывод уникальных значений колонки через .unique()")
    print("\nВсе профессии отцов учеников:")
    print(df["Fjob"].unique())


def index(df):
    print("\n2.14 Удалите текущий индекс и создайте новый индекс на базе новой колонки, которая для этого лучше всего "
          "подходит")
    df.reset_index(drop=True, inplace=True)
    df.insert(loc=0, column='id', value=range(395))
    df.set_index('id', inplace=True)
    print(df.head(10))
