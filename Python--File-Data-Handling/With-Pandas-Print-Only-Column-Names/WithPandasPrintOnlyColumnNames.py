import pandas as pd
result_set = pd.read_csv('Machine_readable_file_bd_employ.csv', sep=',', encoding='utf8')
column_names = result_set.columns
print("Following are the columns names (Header) :- \n")
print(column_names)

'''
Output:

Following are the columns names (Header) :- 

Index(['Series_reference', 'Period', 'Data_value', 'Suppressed', 'STATUS',
       'UNITS', 'Magnitude', 'Subject', 'Group', 'Series_title_1',
       'Series_title_2', 'Series_title_3', 'Series_title_4', 'Series_title_5'],
      dtype='object')

Process finished with exit code 0

'''