import cx_Oracle
# following example is from a locally installed Oracle DB
connection = cx_Oracle.connect('SYSTEM/Black0ps@orcl')
print("Python is connected to Oracle Version of " + connection.version)

connection.close()