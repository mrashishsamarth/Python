import pandas as pd
result_set = pd.read_csv('Machine_readable_file_bd_employ.csv', sep=',', encoding='utf8')
print(result_set.columns)
print()
column_exists = ('ASHISH' in result_set.columns)
print("Does the column 'ASHISH' exists in the CSV file ? " + str(column_exists))
column_exists = ('Period' in result_set.columns)
print("Does the column 'Period' exists in the CSV file ? " + str(column_exists))

'''
Output:
Index(['Series_reference', 'Period', 'Data_value', 'STATUS'], dtype='object')

Does the column 'ASHISH' exists in the CSV file ? False
Does the column 'Period' exists in the CSV file ? True

Process finished with exit code 0

'''