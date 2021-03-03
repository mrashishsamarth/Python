# Import cx_Oracle module for connection
import cx_Oracle
# Import pprint module for pretty printing (it will result in CSV type of format) without the column headers
from pprint import pprint

connection = cx_Oracle.connect('username/password@sid')
cursor = connection.cursor()
sql = "Select * from V$ACCESS where type = 'PACKAGE' and rownum <=10"
cursor.execute(sql)
# Fetch one / first record the records matching the criteria defined in the SQL statement via the cursor
result = cursor.fetchone()
pprint(result)
# Always remember to close the connection.
connection.close()


'''
Output:

(7, 'SYS', 'PLITBLM', 'PACKAGE', 1)

Process finished with exit code 0

'''