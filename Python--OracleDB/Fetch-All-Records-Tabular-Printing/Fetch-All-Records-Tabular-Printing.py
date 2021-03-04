# Use cx_Oracle module for Oracle Connection similar to pymongo for MongoDB
# If cx_Oracle is not installed, execute - "pip install cx_Oracle" on the terminal
import cx_Oracle
# To see a well formatted output of the SQL query use "tabulate" module
from tabulate import tabulate

try:
    connection = cx_Oracle.connect('SYSTEM/Black0ps@orcl')
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

