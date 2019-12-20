import mysql.connector
db = mysql.connector.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="Password1234",  # your password
                    )        # name of the data base

mycursor = db.cursor()

# executing cursor with execute method and pass SQL query
mycursor.execute("CREATE DATABASE preethi")

# get list of all databases
mycursor.execute("SHOW DATABASES")

#print all databses
for x in mycursor:
	print(x)

db.close()
