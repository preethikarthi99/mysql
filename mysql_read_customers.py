'''
Created on Apr 20, 2017
@author: Preethi
'''

#!/usr/bin/python
import base64
import sys
import codecs
import mysql.connector

db = mysql.connector.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="Password1234",  # your password
                     db="preethi")        # name of the data base

cur = db.cursor()

# Use all the SQL you like
cur.execute("select * from customers")

# print all the first cell of all the rows
counter = 0;
for row in cur.fetchall():
    try:
        counter = counter + 1;
        name = str(row[1]);
        address = str(row[2]);
        print(str(counter) + " - " +  name + " - " + address);
    except ValueError as e:
        print('Error');

db.close()