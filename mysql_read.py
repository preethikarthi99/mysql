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
                     db="world")        # name of the data base

#print(db)

if(db):
    print("connected")
# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("select * from city")

# print all the first cell of all the rows
counter = 0;
for row in cur.fetchall():
    try:
        counter = counter + 1;
        title = str(row[2]);
        company = str(row[3]);
        print(str(counter) + " - " +  title + " - " + company);
    except ValueError as e:
        print('Error');

db.close()