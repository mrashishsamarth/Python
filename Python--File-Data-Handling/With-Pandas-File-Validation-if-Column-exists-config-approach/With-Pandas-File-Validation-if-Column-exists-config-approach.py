import pandas as pd
import column_list
result_set = pd.read_csv(r'source_file/Machine_readable_file_bd_employ.csv', sep=',', encoding='utf8')
# print(result_set.columns)
column_exists = None
for item in column_list.col:
    print("Does the column " + item + " exists in the CSV file ? :- " + str(item in result_set.columns))

'''

Does the column Series_reference exists in the CSV file ? :- True
Does the column Period exists in the CSV file ? :- True
Does the column Data_value exists in the CSV file ? :- True
Does the column STATUS exists in the CSV file ? :- True

Process finished with exit code 0

'''