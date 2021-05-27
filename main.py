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

    return render_template("a_tablo.html") 


@app.route("/yontem_1",methods = ["POST","GET"])  
def yontem_1():
    if request.method == "POST":  
        try:  
            p = request.form["p"] 
            l = request.form["l"] 
            celik_sinifi = request.form["celik_sinifi"]
            kesit = request.form["kesit"]

            p=float(p)
            l=float(l)
            celik_sinifi=float(celik_sinifi)

            mycursor.execute("SELECT * FROM a WHERE kesit='{}'".format(kesit))
            satir= mycursor.fetchall()
            print(satir)
            mydb.commit()

            maksimum_sehim=(p*(l**3))/(48*200000*float(satir[0][15])*(10**4))
            print(maksimum_sehim)

            maksimum_moment=(p*l*1000)/(4)
            print(maksimum_moment)

            zati_sehim=((5*float(satir[0][1])*(9.81/1000)*(l**4))/(384*200000*(float(satir[0][15])*(10**4))))
            print(zati_sehim)

            zati_moment=(float(satir[0][1])*(l**2))/(8)
            print(zati_moment)

            toplam_sehim=( zati_sehim + maksimum_sehim)
            print(toplam_sehim)

            toplam_moment=(maksimum_moment+zati_moment)
            print(toplam_moment)

            akma_sinir_durumu=(celik_sinifi*float(satir[0][17])/1.67)
            print(akma_sinir_durumu)

            if (akma_sinir_durumu > toplam_moment) and (l/300 > toplam_sehim):
                uygun_mu="UYGUN"
                print(uygun_mu)
            else:
                # kesit değiştirme yapılacak
                uygun_mu="UYGUN DEĞİL"
                print(uygun_mu)
                pass




       
            return render_template("a_tablo.html", uygun_mu = uygun_mu) 
        except: 
            return render_template("a_tablo.html") 


if __name__ == '__main__':
    #app.debug = True
    app.run(host="0.0.0.0", port="8080")
  
