# Import cx_Oracle module for connection
import cx_Oracle
# Import pprint module for pretty printing (it will result in CSV type of format) without the column headers
from pprint import pprint

connection = cx_Oracle.connect('username/password@sid')
cursor = connection.cursor()
sql = "Select * from V$ACCESS where type = 'PACKAGE'"
cursor.execute(sql)
# Fetch all the records matching the criteria defined in the SQL statement via the cursor
result = cursor.fetchall()
pprint(result)
# Always remember to close the connection.
connection.close()

