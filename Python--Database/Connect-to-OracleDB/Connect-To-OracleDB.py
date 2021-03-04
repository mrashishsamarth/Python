# Use cx_Oracle library for Oracle Connection similar to pymongo for MongoDB
import cx_Oracle
from tabulate import tabulate

try:
    connection = cx_Oracle.connect('username/password@sid')
    cursor = connection.cursor()
    cursor.execute("Select * from V$ACCESS where rownum <= 10")
    res = cursor.fetchall()
    # Use tabulate library to print the output similar to SQL Developer or Toad
    print(tabulate(res, headers=['SID', 'OWNER', 'OBJECT', 'TYPE', 'CON_ID'], tablefmt='psql'))

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