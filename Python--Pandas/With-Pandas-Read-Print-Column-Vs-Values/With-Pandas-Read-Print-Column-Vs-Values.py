import pandas as pd
result_set = pd.read_csv('Machine_readable_file_bd_employ.csv', sep=',', encoding='utf8')
print(result_set.count())