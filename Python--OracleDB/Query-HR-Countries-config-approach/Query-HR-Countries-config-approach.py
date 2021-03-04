# Import cx_Oracle module for connection
import cx_Oracle
import conf
import sql
from tabulate import tabulate

connection = cx_Oracle.connect(conf.user, conf.password, conf.sid)
cursor = connection.cursor()
cursor.execute(sql.query)
# Fetch all the records matching the criteria defined in the SQL statement via the cursor
result = cursor.fetchall()
print(tabulate(result, headers=['COUNTRY_ID', 'COUNTRY_NAME', 'REGION_ID'], tablefmt='psql'))
# Always remember to close the connection.
connection.close()
