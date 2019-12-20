import mysql.connector
db = mysql.connector.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="Password1234",  # your password
                     db="preethi")        # name of the data base

mycursor = db.cursor()

# executing cursor with execute method and pass SQL query
mycursor.execute("USE preethi")

# get list of all databases
mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

#get list of all tables
mycursor.execute("SHOW TABLES")

#print my table
for x in mycursor:
	print(x)

db.close()
