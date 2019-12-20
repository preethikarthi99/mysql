
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
    
def get_db_cursor():
    db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="Password1234",  # your password
                     db="preethi")        # name of the data base

    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    return db.cursor()


'''
    Add customers
'''
def add_customers(db, name, address):
    
    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    cur = db.cursor()
    
    #
    sql = "INSERT INTO customers (NAME, ADDRESS) VALUES (%s, %s)"
    values = (name, address)

    # Use all the SQL you like
    cur.execute(sql, values)

    db.commit()

    print('Done : '+str(cur.rowcount)+" inserted") 
    
    
'''
    Update customers
'''    
def update_customers(db, name, address, id):
    
    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    cur = db.cursor()
    
    #
    sql = "UPDATE customers SET NAME = %s, ADDRESS = %s WHERE ID = %s"
    values = (name, address, id)

    # Use all the SQL you like
    cur.execute(sql, values)

    db.commit()

    print('Done : '+str(cur.rowcount)+" updated") 

    read_customers(db)


'''
    Delete customers
'''    
def delete_customers(db, id):
    
    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    cur = db.cursor()
    
    #
    sql = "DELETE FROM customers WHERE ID = %s"
    values = (id, )

    # Use all the SQL you like
    cur.execute(sql, values)

    db.commit()
    
    if(cur.rowcount == 0):
        raise Exception("Item Not Available to Delete")
    
    if(cur.rowcount > 1):
        raise Exception("More than one item deleted")

    print('Done : '+str(cur.rowcount)+" deleted")   
    read_customers(db)         


'''
    Read customers
'''
def read_customers(db):
    
    cur = db.cursor()
    
    # Use all the SQL you like
    cur.execute("SELECT * FROM customers")

    # print all the first cell of all the rows
    counter = 0;
    for row in cur.fetchall():
        try:
            counter = counter + 1
        
            pid = str(row[0])
            name = str(row[1])
            address = str(row[2])
            
            print(pid + " - " +  name + " - " +address)
        except ValueError as error:
            print('Error', format(error))

    

def main():
    
    db = get_db()
    
    # C - add customers
    add_customers(db, "Yuvi", "Perungalathur")
    
    # R - read customers
    read_customers(db)
    
    # U - update customers
    update_customers(db, "Swathi", "Tambaram", 6)
    
    # D - delete customers
    try:
        delete_customers(db, 7)
    except Exception as er:
        print("Error : ", format(er))
    
    # close DB
    db.close()

if __name__ == '__main__':
    main()

