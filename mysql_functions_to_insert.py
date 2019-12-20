'''
Created on Apr 20, 2017
@author: Preethi
source:
    https://www.w3schools.com/python/python_mysql_insert.asp
'''

#!/usr/bin/python
import base64
import sys
import codecs
import MySQLdb


def get_db():

    db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="Password1234",  # your password
                     db="preethi")        # name of the data base
    
    return db

def insert_customers(db, name, address):
    
    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    cur = db.cursor()
    
    #
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    values = (name, address)

    # Use all the SQL you like
    cur.execute(sql, values)

    db.commit()

    print('Done : '+str(cur.rowcount)+" inserted")
    

def main():
    
    db = get_db();
    
    insert_customers(db, "Ponni", "Gandhi nagar")
    insert_customers(db, "Siva", "Iyyencherry")
    
    db.close()

if __name__ == '__main__':
    main()