import mysql.connector


print("VERİTABANI YÜKLENİYOR..")
mydb = mysql.connector.connect(
  host="remotemysql.com",
  user="P0xYObZY55",
  password="3bT6PmoVEb",
  database="P0xYObZY55"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE IF NOT EXISTS xxxxxxxxx")

mycursor.execute("CREATE TABLE IF NOT EXISTS a (id INT AUTO_INCREMENT PRIMARY KEY, isim VARCHAR(25))")
