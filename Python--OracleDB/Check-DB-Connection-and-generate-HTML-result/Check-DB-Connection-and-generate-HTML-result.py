import cx_Oracle
import time
from datetime import datetime

SID = ['DB-1', 'DB-2', 'DB-3', 'DB-4', 'DB-5', 'DB-6', 'DB-7', 'DB-8', 'DB-9', 'DB-10']
username = 'SYSTEM'
password = 'Black0ps'
sql = "SELECT TO_CHAR(SYSDATE, 'MM/DD/YYYY HH24:MI:SS') FROM DUAL"
now = datetime.now()
with open('connection_result.html', 'w') as file:
    for item in SID:
        connection = cx_Oracle.connect(username, password, cx_Oracle.makedsn('127.0.0.1', 1521, 'orcl'))
        cursor = connection.cursor()
        cursor.execute(sql)
        result = str(cursor.fetchone())
        connection_timestamp = result.rstrip(',)').lstrip('(')
        connection.close()
        time.sleep(2)
        file.write("<pre>" + "Connected to " + str(item) + " at " + connection_timestamp + " successfully" + "</pre>")
execution_complete = now.strftime("%d/%m/%Y %H:%M:%S")
print(f"Script Execution Completed at {execution_complete}")

