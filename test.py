import mysql.connector
from flask import Flask, render_template, request

print("VERİTABANI YÜKLENİYOR..")

mydb = mysql.connector.connect(
  host="remotemysql.com",
  user="P0xYObZY55",
  password="3bT6PmoVEb",
  database="P0xYObZY55"
)
mycursor = mydb.cursor()

  

mycursor.execute("SELECT G,h,b FROM a")
satir_temp = mycursor.fetchall()
satir=[]
for i in satir_temp:
    print(float(i[0])+float(i[1])+float(i[2]))
mydb.commit()

  
