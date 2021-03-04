import cx_Oracle
# following example is from a locally installed Oracle DB
connection = cx_Oracle.connect('username/password@sid')
print("Python is connected to Oracle Version of " + connection.version)
connection.close()

'''
Output:
Python is connected to Oracle Version of 19.3.0.0.0

'''
