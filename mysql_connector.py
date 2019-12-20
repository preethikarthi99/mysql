'''
Created on Apr 20, 2017
@author: Preethi
'''

#!/usr/bin/python
import mysql.connector

db = mysql.connector.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="Password1234",  # your password
                     db="world")        # name of the data base

print(db)

mycursor = db.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)

db.close()