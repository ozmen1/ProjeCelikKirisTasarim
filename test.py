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



def max_sehim():
  p=float(input("P değerini giriniz: "))
  l=float(input("L değerini giriniz: "))
  kesit=(input("kesit giriniz"))
  mycursor.execute("SELECT * FROM a WHERE kesit='{}'".format(kesit))
  satir= mycursor.fetchall()
  # print(satir)
  # print(satir[0][15])
  mydb.commit()

  maksimum_sehim=(p*(l**3))/(48*200000*float(satir[0][15])*(10**4))
  print("MAKSİMUM SEHİM : ", float(maksimum_sehim))
  return maksimum_sehim




def max_moment():
  p=float(input("P değerini giriniz: "))
  l=float(input("L değerini giriniz: "))

  maksimum_moment=(p*l*1000)/(4)

  print("MAKSİMUM MOMENT : ", float(maksimum_moment))
  return maksimum_moment



def zati_sehim():
  l=float(input("L değerini giriniz: "))
  kesit=(input("kesit giriniz"))
  mycursor.execute("SELECT * FROM a WHERE kesit='{}'".format(kesit))
  satir= mycursor.fetchall()
  # print(satir)
  # print(satir[0][1])
  # print(satir[0][15])
  mydb.commit()

  zati_sehim=((5*float(satir[0][1])*(9.81/1000)*(l**4))/(384*200000*(float(satir[0][15])*(10**4))))
  print("zati sehim : ", zati_sehim)
  return zati_sehim




def zati_moment():
  l=float(input("L değerini giriniz: "))
  kesit=(input("kesit giriniz"))
  mycursor.execute("SELECT * FROM a WHERE kesit='{}'".format(kesit))
  satir= mycursor.fetchall()
  # print(satir)
  # print(satir[0][1])
  mydb.commit()
  zati__moment=(float(satir[0][1])*(l**2))/(8)
  print("ZATİ MOMENT : ",zati__moment)
  return zati__moment


def toplam_sehim():
  # def zati_sehim():  ile  def max_sehim():   toplanacak 

  toplam_sehim=( zati_sehim() + max_sehim())
  print("TOPLAM SEHİM : ", toplam_sehim)
  return toplam_sehim


def toplam_moment():
  # def max_moment(): ile   def zati_moment():   toplanacak

  toplam_moment=(max_moment()+zati_moment())
  print("TOPLAM MOMENT : ", toplam_moment)



def akma_sinir_durumu():
  kesit=(input("kesit giriniz"))
  celik_sinifi=float(input("ÇELİK SINIFI DEĞERİNİ GİRİNİZ"))
  mycursor.execute("SELECT * FROM a WHERE kesit='{}'".format(kesit))
  satir= mycursor.fetchall()
  # print(satir[0][17])
  mydb.commit()
  a_s_durumu=(celik_sinifi*float(satir[0][17])/1.67)
  print("AKMA SINIR DURUMU : ", a_s_durumu)
  return a_s_durumu


if (akma_sinir_durumu > toplam_moment) and (l/300 > toplam_sehim):
  print("uygun")
else:
  # kesit değiştirme yapılacak
  pass





# max_sehim()
# max_moment()
# zati_sehim()
# zati_moment()
# toplam_sehim()
# toplam_moment()
# akma_sinir_durumu()
