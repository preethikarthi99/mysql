import mysql.connector
db = mysql.connector.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="Password1234",  # your password
                     db="preethi")        # name of the data base

mycursor = db.cursor()

# executing cursor with execute method and pass SQL query
mycursor.execute("USE preethi")

#insert query
query = "INSERT INTO customers ( name, address) VALUES ( %s, %s)"

#values
val = [
  ("Roopa", "Lowstreet 4"),
  ("Preethi", "Apple st 652"),
  ("Hema", "Mountain 21"),
  ("Mana", "Valley 345"),
  ("Sudha", "Ocean blvd 2"),
  ("Badma", "Green Grass 1"),
  ("Raja", "Sky st 331"),
  ("Sam", "One way 98"),
]

#insert into table customers
mycursor.executemany(query , val)

#commit into database
db.commit()

#print the number of rows inserted
print(mycursor.rowcount, "record inserted.")

db.close()
