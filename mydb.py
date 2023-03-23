#Install MySQL on your computer
#Go to community downloads of mysql workbench
#pip install mysql
#pip install mysql-connector
#pip install mysql-connector-python

import mysql.connector

database = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'Ishan@0209'

	)

#Prepare a cursor object
cursorObject = database.cursor()

#Create a database
cursorObject.execute("CREATE database elderco")

print("All Done")
