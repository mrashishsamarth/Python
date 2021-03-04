# Import cx_Oracle module for connection
import cx_Oracle
# Import pprint module for pretty printing (it will result in CSV type of format) without the column headers
from pprint import pprint

connection = cx_Oracle.connect('username/password@orcl')
cursor = connection.cursor()
sql = "Select * from V$ACCESS where type = 'PACKAGE'"
cursor.execute(sql)
# Fetch all the records matching the creteria defined in the SQL statement via the cursor
result = cursor.fetchall()
pprint(result)
# Always remember to close the connection.
connection.close()


'''
Output:
[(7, 'SYS', 'PLITBLM', 'PACKAGE', 1),
 (7, 'SYS', 'UTL_RAW', 'PACKAGE', 1),
 (7, 'SYS', 'DBMS_DDL', 'PACKAGE', 1),
 (7, 'SYS', 'DBMS_SQL', 'PACKAGE', 1),
 (7, 'SYS', 'STANDARD', 'PACKAGE', 1),
 (7, 'SYS', 'UTL_FILE', 'PACKAGE', 1),
 (7, 'SYS', 'DBMS_LOCK', 'PACKAGE', 1),
 (7, 'SYS', 'UTL_IDENT', 'PACKAGE', 1),
 (7, 'SYS', 'UTL_RECOMP', 'PACKAGE', 1),
 (7, 'SYS', 'DBMS_ASSERT', 'PACKAGE', 1)]

Process finished with exit code 0

'''