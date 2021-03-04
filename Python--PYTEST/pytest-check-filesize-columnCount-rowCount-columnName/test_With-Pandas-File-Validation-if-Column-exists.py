# Import os module since we are using the getsize to get the file size of the CSV
import os
# Import pandas module to to read the csv and extract the needed values for test cases
import pandas as pd

# Provide the absolute path of the csv file
source_file = 'Machine_readable_file_bd_employ.csv'
# Reading the content of the file in the result set
result_set = pd.read_csv('Machine_readable_file_bd_employ.csv', sep=',', encoding='utf8')
# Create a list to have the column names for validation against the headers extracted from the CSV file
col = ['Series_reference', 'Period', 'Data_value', 'STATUS']


# Following test case will check if the file  size of the CSV is greater than zero
def test_case_1():
    assert os.path.getsize(source_file) > 0


# Following test case will check if the number of rows in the CSV is greater than 1, since we have to exclude the header
def test_case_2():
    assert result_set.shape[0] > 1


# Following test case will check if the number of column in the CSV is equal to 4 and matches the design specifications
def test_case_3():
    assert result_set.shape[1] == 4


# Following test case will check if the columns names in CSV are same as in the provided reference list to comparison
for item in col:
    # Against each element in the list col, run the following test cases
    def test_case_4():
        assert item in result_set.columns


'''
Output:


C:\Users\Groot\IdeaProjects\Python\Python--PYTEST\pytest-check-filesize-columnCount-rowCount-columnName>pytest
================================================================================= test session starts ==================================================================================
platform win32 -- Python 3.9.2, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
rootdir: C:\Users\Groot\IdeaProjects\Python\Python--PYTEST\pytest-check-filesize-columnCount-rowCount-columnName
collected 4 items                                                                                                                                                                       

test_With-Pandas-File-Validation-if-Column-exists.py ....                                                                                                                         [100%]

================================================================================== 4 passed in 4.34s ===================================================================================

C:\Users\Groot\IdeaProjects\Python\Python--PYTEST\pytest-check-filesize-columnCount-rowCount-columnName>



'''