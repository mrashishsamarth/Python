import cx_Oracle
from tabulate import tabulate

try:
    connection = cx_Oracle.connect('username/password@sid')
    cursor = connection.cursor()
    # To print specific column value in the output, just select that column in the query
    sql = "Select SID from V$ACCESS where rownum <= 10"
    cursor.execute(sql)
    result = cursor.fetchall()
    # Headers will utilized as the column name
    print(tabulate(result, headers=['SID'], tablefmt='psql'))

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()


'''
Output:
+-------+
|   SID |
|-------|
|     6 |
|     6 |
|     6 |
|     7 |
|     7 |
|     7 |
|     7 |
|     7 |
|     7 |
|     7 |
+-------+


'''