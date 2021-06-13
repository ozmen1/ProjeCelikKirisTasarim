import mysql.connector
import xlrd

print("VERİTABANI YÜKLENİYOR..")
mydb = mysql.connector.connect(
  host="remotemysql.com",
  user="P0xYObZY55",
  password="3bT6PmoVEb",
  database="P0xYObZY55"
)

mycursor = mydb.cursor()

""" #mycursor.execute("CREATE DATABASE IF NOT EXISTS xxxxxxxxx")



wb = xlrd.open_workbook('ProjeCelikKirisTasarim/a.xls')
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)
baslik=sheet.row_values(0)
print(baslik) """

""" # başlık eklemek için
mycursor.execute("CREATE TABLE IF NOT EXISTS a (kesit VARCHAR(50) PRIMARY KEY)".format(sheet.row_values(0)[0]))
for i in range(1,27):
  mycursor.execute("ALTER TABLE a ADD COLUMN {} TEXT".format(sheet.row_values(0)[i]))
  mydb.commit() """



""" for j in range(1,111):
  print(j)
  satir=sheet.row_values(j)
  print(satir)
  mycursor.execute("INSERT INTO a VALUE ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(satir[0], satir[1], satir[2], satir[3], satir[4], satir[5], satir[6], satir[7], satir[8], satir[9], satir[10], satir[11], satir[12], satir[13], satir[14], satir[15], satir[16], satir[17], satir[18], satir[19], satir[20], satir[21], satir[22], satir[23], satir[24], satir[25], satir[26]))
  mydb.commit() """



""" for j in range(1,111):
  print(j)
  satir=sheet.row_values(j)
  print(satir)
  for i in range(27):
    print(baslik[i], satir[i])
    mycursor.execute("INSERT INTO a ('{0}') VALUE ('{1}',)".format(baslik[i], satir[i]))
    mydb.commit() """



""" mycursor.execute("SELECT * FROM a")
for x in mycursor.fetchall():
    print(x)
mydb.commit()

x=input("") """

mycursor.execute("SELECT kesit FROM a")
satir= mycursor.fetchall()
satir_liste=[]
for i in range(len(satir)):
  print(satir[i][0])
  satir_liste.append(satir[i][0])


print(satir_liste,sep="\n")


mydb.commit()