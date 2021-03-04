import pandas as pd
result_set = pd.read_csv('Machine_readable_file_bd_employ.csv', sep=',', encoding='utf8')
column_names = result_set.columns
print("Following are the columns names (Header) :- \n")
print(column_names)