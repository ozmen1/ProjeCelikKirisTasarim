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

    global satir_liste

    mycursor.execute("SELECT kesit FROM a")
    satir_temp= mycursor.fetchall()
    satir_liste=[]
    for i in range(len(satir_temp)):
        #print(satir_temp[i][0])
        satir_liste.append(satir_temp[i][0])
    #print(satir_liste)
    mydb.commit()

    return render_template("a_tablo.html", satir_liste=satir_liste) 

@app.route('/yontem_2.html')
def yontem2():


    return render_template("yontem_2.html") 


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
            #print(satir)
            mydb.commit()

            maksimum_sehim=(p*(l*1000)**3)/(48*200000*float(satir[0][15])*(10**4))
            print("maksimum sehim :",maksimum_sehim)

            maksimum_moment=(p*l)/(4)
            print("maksimum moment :",maksimum_moment)

            zati_sehim=((5*float(satir[0][1])*(9.81/1000)*(l*1000)**4)/(384*200000*(float(satir[0][15])*(10**4))))
            print("zati sehim :",zati_sehim)

            zati_moment=(float(satir[0][1])*9.81*(l**2))/(8)
            print("zati moment :",zati_moment)

            toplam_sehim=( zati_sehim + maksimum_sehim)
            print("toplam sehim",toplam_sehim)

            toplam_moment=(maksimum_moment+zati_moment)
            print("toplam moment :",toplam_moment)

            akma_sinir_durumu=(celik_sinifi*float(satir[0][17])/1.67)
            print("akma sınır durumu :",akma_sinir_durumu)

            if ((akma_sinir_durumu > toplam_moment) and ((l*1000/300) > toplam_sehim)):
                uygun_mu="UYGUN"
                print(uygun_mu)
            else:
                # kesit değiştirme yapılacak
                uygun_mu="UYGUN DEĞİL"
                print(uygun_mu)

       
            return render_template("a_tablo.html", satir_liste=satir_liste, p=p, l=l, kesit=kesit, celik_sinifi=celik_sinifi, uygun_mu = uygun_mu) 
        except:
            uygun_mu="GEÇERLİ DEĞER GİRİLMEDİ"
            print(uygun_mu)
            return render_template("a_tablo.html", satir_liste=satir_liste, uygun_mu=uygun_mu) 


################################################################################################--2


@app.route("/yontem_2",methods = ["POST","GET"])  
def yontem_2():
    if request.method == "POST":
      try:
        p = request.form["p"] 
        l = request.form["l"] 
        celik_sinifi = request.form["celik_sinifi"]
        kesit_tipi = request.form["kesit_tipi"]
    

        p=float(p)
        l=float(l)
        celik_sinifi=float(celik_sinifi)

        maksimum_moment=(p*l)/(4)
        print("maksimum moment :",maksimum_moment)

        wp_gerekli=maksimum_moment*1.67/celik_sinifi
        print("Wp gerekli : ",wp_gerekli)

        mycursor.execute("SELECT * FROM a")
        satir= mycursor.fetchall()
        mydb.commit()

        satir_dict={}

        for i in range(len(satir)):
            #print(satir[i][0])
            #print(kesit_tipi)

            if kesit_tipi in satir[i][0]:
                satir_dict[satir[i][0]]=satir[i][17]
        #print(satir_dict)
        
        while True:
          fark=100000000000000000000000
          for x, y in satir_dict.items():                
              #print(x, y)
              if wp_gerekli<=float(y):
                  fark_temp=float(y)-wp_gerekli
                  if fark>fark_temp:
                      fark=fark_temp
                      kesit_2=x
          print("kesit_2 :",kesit_2)


          mycursor.execute("SELECT * FROM a WHERE kesit='{}'".format(kesit_2))
          satir_2= mycursor.fetchall()
          #print(satir)
          mydb.commit()

          zati_sehim=((5*float(satir_2[0][1])*(9.81/1000)*(l*1000)**4)/(384*200000*(float(satir_2[0][15])*(10**4))))
          print("zati sehim :",zati_sehim)

          zati_moment=(float(satir_2[0][1])*9.81*(l**2))/(8)
          print("zati moment :",zati_moment)

          maksimum_sehim=(p*(l*1000)**3)/(48*200000*float(satir_2[0][15])*(10**4))
          print("maksimum sehim :",maksimum_sehim)

          toplam_sehim=( zati_sehim + maksimum_sehim)
          print("toplam sehim :",toplam_sehim)

          toplam_moment=(maksimum_moment+zati_moment)
          print("toplam moment :",toplam_moment)

          akma_sinir_durumu=(celik_sinifi*float(satir_2[0][17])/1.67)
          print("akma sınır durumu :",akma_sinir_durumu)

          if ((akma_sinir_durumu > toplam_moment) and ((l*1000/300) > toplam_sehim)):
              uygun_mu="UYGUN"
              print(uygun_mu)
              return render_template("yontem_2.html", kesitt=kesit_2, uygun_mu=uygun_mu)
          elif len(satir_dict)>0:
              satir_dict.pop(kesit_2)
              continue
          else:
            uygun_mu="VERİ TABANINDA UYGUN KESİT BULUNAMADI"
            print(uygun_mu)
            return render_template("yontem_2.html", uygun_mu=uygun_mu)

          
      except:
        uygun_mu="GEÇERLİ DEĞER GİRİLMEDİ"
        print(uygun_mu)
        return render_template("yontem_2.html", uygun_mu=uygun_mu)












if __name__ == '__main__':
    #app.debug = True
    app.run(host="0.0.0.0", port="8080")
  





