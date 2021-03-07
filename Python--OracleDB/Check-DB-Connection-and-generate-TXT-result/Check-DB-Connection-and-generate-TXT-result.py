import cx_Oracle
from datetime import datetime
from contextlib import redirect_stdout

SID = ['DB-1', 'DB-2', 'DB-3', 'DB-4', 'DB-5', 'DB-6', 'DB-7', 'DB-8', 'DB-9', 'DB-10']
username = 'SYSTEM'
password = 'Black0ps'
sql = "SELECT TO_CHAR(SYSDATE, 'MM/DD/YYYY HH24:MI:SS') FROM DUAL"
now = datetime.now()

with open('connection_result.txt', 'w') as file:
    with redirect_stdout(file):
        for item in SID:
            connection = cx_Oracle.connect(username, password, cx_Oracle.makedsn('127.0.0.1', 1521, 'orcl'))
            cursor = connection.cursor()
            cursor.execute(sql)
            result = str(cursor.fetchone())
            connection_timestamp = result.rstrip(',)').lstrip('(')
            print(f"Connected to {item} at {connection_timestamp} successfully")
            connection.close()

execution_complete = now.strftime("%d/%m/%Y %H:%M:%S")
print(f"Script Execution Completed at {execution_complete}")