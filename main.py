import mysql.connector
from flask import Flask, render_template, request
import xlrd



print("VERİTABANI YÜKLENİYOR..")

mydb = mysql.connector.connect(
  host="remotemysql.com",
  user="P0xYObZY55",
  password="3bT6PmoVEb",
  database="P0xYObZY55"
)

mycursor = mydb.cursor()



app = Flask(__name__)

@app.route('/', methods = ["POST","GET"])
def giris_ekran():
    mycursor.execute("SELECT * from a")   
    satir = mycursor.fetchall() 
    print(satir)

    wb = xlrd.open_workbook('ProjeCelikKirisTasarim/a.xls')
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)
    baslik=sheet.row_values(0)
    print(baslik)
    return render_template("a_tablo.html", rows = satir, cols = baslik) 




if __name__ == '__main__':
    #app.debug = True
    app.run(host="0.0.0.0", port="8080")
  
