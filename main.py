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



app = Flask(__name__)

@app.route('/')
def giris_ekran():
    mycursor.execute("SELECT kesit FROM a")
    kesitler = mycursor.fetchall()
    print(kesitler)
    mydb.commit()
  


    return render_template("a_tablo.html", kesitler=kesitler) 


@app.route("/sec",methods = ["POST","GET"])  
def sec():
    if request.method == "POST":  
        try:  
            secim = request.form["secim"]  

            mycursor.execute("SELECT * FROM a WHERE kesit='{}'".format(secim))
            satir_temp = mycursor.fetchall()
            satir=[]
            for i in satir_temp:
                satir.append(i)
            print(satir)
            mydb.commit()

            
       
            return render_template("a_tablo.html", rows = satir) 
        except: 
            return render_template("a_tablo.html") 


if __name__ == '__main__':
    #app.debug = True
    app.run(host="0.0.0.0", port="8080")
  
