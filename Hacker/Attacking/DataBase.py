import mysql.connector

con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="abebaws"
)
if con.is_connected():
    print("Connected to MySQL database")

cur=con.cursor()

cur.execute("create database if not exists TryH")
print("Database is created")
cur.execute("use TryH")
cur.execute("CREATE TABLE hack if not exists (id INT AUTO_INCREMENT PRIMARY KEY, user VARCHAR(255), pass VARCHAR(255))")
print("Tabel is created")

