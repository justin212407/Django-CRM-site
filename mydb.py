import mysql.connector 

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'Aaloo@2124',
	auth_plugin='mysql_native_password'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE elederco")

print("ALL DONE")