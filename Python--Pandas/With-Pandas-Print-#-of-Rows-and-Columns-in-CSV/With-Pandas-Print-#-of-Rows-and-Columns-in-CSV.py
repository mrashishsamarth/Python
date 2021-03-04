import pandas as pd
result_set = pd.read_csv('Machine_readable_file_bd_employ.csv', sep=',', encoding='utf8')
column_names = result_set.shape
print("Number of Rows in this csv file is :- " + str(column_names[0]))
print("Number of Columns in this csv file is :- " + str(column_names[1]))
