import pandas as pd
result_set = pd.read_csv('Machine_readable_file_bd_employ.csv',sep=',', encoding='utf8')
print(result_set.columns)
print()
column_exists = ('ASHISH' in result_set.columns)
print("Does the column 'ASHISH' exists in the CSV file ? " + str(column_exists))
column_exists = ('Period' in result_set.columns)
print("Does the column 'Period' exists in the CSV file ? " + str(column_exists))
