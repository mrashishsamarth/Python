import pandas as pd
result_set = pd.read_csv('Machine_readable_file_bd_employ.csv', sep=',', encoding='utf8')
print(result_set.count())


'''
Output:

Series_reference    37
Period              37
Data_value          37
Suppressed           6
STATUS              37
UNITS               37
Magnitude           37
Subject             37
Group               37
Series_title_1      37
Series_title_2      37
Series_title_3      37
Series_title_4       3
Series_title_5       2

dtype: int64

Process finished with exit code 0


'''