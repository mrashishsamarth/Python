# Use cx_Oracle module for Oracle Connection similar to pymongo for MongoDB
# If cx_Oracle is not installed, execute - "pip install cx_Oracle" on the terminal
import cx_Oracle
# To see a well formatted output of the SQL query use "tabulate" module
from tabulate import tabulate

try:
    connection = cx_Oracle.connect('username/password@sid')
    cursor = connection.cursor()
    sql = "Select * from V$ACCESS where rownum <= 10"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(tabulate(result, headers=['SID', 'OWNER', 'OBJECT', 'TYPE', 'CON_ID'], tablefmt='psql'))

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()


"""
Output looks like the following
+-------+---------+----------+--------+----------+
|   SID | OWNER   | OBJECT   | TYPE   |   CON_ID |
|-------+---------+----------+--------+----------|
|     6 |         | DVSYS    | NONE   |        1 |
|     6 | SYS     | DUAL     | TABLE  |        1 |
|     6 | DVSYS   | DV_AUTH$ | TABLE  |        1 |
|     7 | SYS     | DUAL     | TABLE  |        1 |
|     7 | SYS     | OBJ$     | TABLE  |        1 |
|     7 | SYS     | TYPE$    | TABLE  |        1 |
|     7 | SYS     | UNDO$    | TABLE  |        1 |
"""