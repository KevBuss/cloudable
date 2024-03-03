import mysql.connector

# Connect to the MySQL server
db = mysql.connector.connect(
  host="c220g5-110505vm-1.wisc.cloudlab.us",
  port='3306',
  user="root",
  password="asdfasdf"
)

print("Successfully connected to MySQL server")

cursor = db.cursor();

cursor.execute('USE csc468')
cursor.execute('SELECT * FROM cattle')

for row in cursor:
    print(row)

cursor.close()
db.close()
