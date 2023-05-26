import functions_list
import pandas as pd

df = pd.read_csv("students.csv")

functions_list.print_table(df)

functions_list.print_table_first5(df)

functions_list.print_table_last5(df)

functions_list.describe(df)

functions_list.find_cell(df)

functions_list.filter_str(df)

functions_list.filter_set(df)

functions_list.nan_add(df)

functions_list.create_field(df)

functions_list.sorting(df)

functions_list.statistics(df)

functions_list.value_counts(df)

functions_list.unique(df)

functions_list.index(df)
