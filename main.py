import mysql.connector
from flask import Flask, render_template, request
from functions import *

app = Flask(__name__)


try:
    print("LOCAL_VERİTABANI YÜKLENİYOR..")
    mydb = mysql.connector.connect(
        host="remotemysql.com",
        user="P0xYObZY55",
        password="3bT6PmoVEb",
        database="P0xYObZY55"
    )
    mycursor = mydb.cursor()
    print("LOCAL_VERİTABANI BAŞARILI ALINDI")

except:
    print("WEB_VERİTABANI YÜKLENİYOR..")
    mydb = mysql.connector.connect(
        host="projecelikkiristasarim.mysql.pythonanywhere-services.com",
        user="projecelikkirist",
        password="8imtr4WtwXGaUp@",
        database="projecelikkirist$P0xYObZY55"
    )
    mycursor = mydb.cursor()
    print("WEB_VERİTABANI BAŞARILI ALINDI")


@app.route('/')
def index():
    try:
        print("LOCAL_VERİTABANI YÜKLENİYOR..")
        mydb = mysql.connector.connect(
            host="remotemysql.com",
            user="P0xYObZY55",
            password="3bT6PmoVEb",
            database="P0xYObZY55"
        )
        mycursor = mydb.cursor()
        print("LOCAL_VERİTABANI BAŞARILI ALINDI")

    except:
        print("WEB_VERİTABANI YÜKLENİYOR..")
        mydb = mysql.connector.connect(
            host="projecelikkiristasarim.mysql.pythonanywhere-services.com",
            user="projecelikkirist",
            password="8imtr4WtwXGaUp@",
            database="projecelikkirist$P0xYObZY55"
        )
        mycursor = mydb.cursor()
        print("WEB_VERİTABANI BAŞARILI ALINDI")
    return render_template("index.html")


@app.route('/yontem_1.html')
def yontem1():
    try:
        print("LOCAL_VERİTABANI YÜKLENİYOR..")
        mydb = mysql.connector.connect(
            host="remotemysql.com",
            user="P0xYObZY55",
            password="3bT6PmoVEb",
            database="P0xYObZY55"
        )
        mycursor = mydb.cursor()
        print("LOCAL_VERİTABANI BAŞARILI ALINDI")

    except:
        print("WEB_VERİTABANI YÜKLENİYOR..")
        mydb = mysql.connector.connect(
            host="projecelikkiristasarim.mysql.pythonanywhere-services.com",
            user="projecelikkirist",
            password="8imtr4WtwXGaUp@",
            database="projecelikkirist$P0xYObZY55"
        )
        mycursor = mydb.cursor()
        print("WEB_VERİTABANI BAŞARILI ALINDI")

    global satir_liste

    mycursor.execute("SELECT kesit FROM a")
    satir_temp = mycursor.fetchall()
    satir_liste = []
    for i in range(len(satir_temp)):
        # print(satir_temp[i][0])
        satir_liste.append(satir_temp[i][0])
    # print(satir_liste)
    mydb.commit()

    return render_template("yontem_1.html", satir_liste=satir_liste)


@app.route('/yontem_2.html')
def yontem2():
    try:
        print("LOCAL_VERİTABANI YÜKLENİYOR..")
        mydb = mysql.connector.connect(
            host="remotemysql.com",
            user="P0xYObZY55",
            password="3bT6PmoVEb",
            database="P0xYObZY55"
        )
        mycursor = mydb.cursor()
        print("LOCAL_VERİTABANI BAŞARILI ALINDI")

    except:
        print("WEB_VERİTABANI YÜKLENİYOR..")
        mydb = mysql.connector.connect(
            host="projecelikkiristasarim.mysql.pythonanywhere-services.com",
            user="projecelikkirist",
            password="8imtr4WtwXGaUp@",
            database="projecelikkirist$P0xYObZY55"
        )
        mycursor = mydb.cursor()
        print("WEB_VERİTABANI BAŞARILI ALINDI")

    return render_template("yontem_2.html")

# --1


@app.route("/yontem_1", methods=["POST", "GET"])
def yontem_1():
    try:
        print("LOCAL_VERİTABANI YÜKLENİYOR..")
        mydb = mysql.connector.connect(
            host="remotemysql.com",
            user="P0xYObZY55",
            password="3bT6PmoVEb",
            database="P0xYObZY55"
        )
        mycursor = mydb.cursor()
        print("LOCAL_VERİTABANI BAŞARILI ALINDI")

    except:
        print("WEB_VERİTABANI YÜKLENİYOR..")
        mydb = mysql.connector.connect(
            host="projecelikkiristasarim.mysql.pythonanywhere-services.com",
            user="projecelikkirist",
            password="8imtr4WtwXGaUp@",
            database="projecelikkirist$P0xYObZY55"
        )
        mycursor = mydb.cursor()
        print("WEB_VERİTABANI BAŞARILI ALINDI")

    if request.method == "POST":
        try:
            p = request.form["p"]
            l = request.form["l"]
            celik_sinifi = request.form["celik_sinifi"]
            kesit = request.form["kesit"]
            yukleme_durumlari = request.form["yukleme_durumlari"]

            p = float(p)
            l = float(l)
            celik_sinifi = float(celik_sinifi)
            yukleme_durumlari = int(yukleme_durumlari)

            mycursor.execute("SELECT * FROM a WHERE kesit='{}'".format(kesit))
            satir = mycursor.fetchall()
            print(satir)
            mydb.commit()

            if yukleme_durumlari == 1:
                print("1_Basit Kiriş - Düzgün Yayılı Yük")
            elif yukleme_durumlari == 7:
                print("7_Basit Kiriş – Merkezde Noktasal Yük")
            elif yukleme_durumlari == 19:
                print("19_Konsol Kiriş – Düzgün Yayılı Yük")
            elif yukleme_durumlari == 22:
                print("22_Konsol Kiriş – Serbest Uçta Noktasal Yük")

            E = 200000  # elastisite modulu (MPa)

            maksimum_sehim = (p*(l*1000)**3)/(48*E *
                                              float(satir[0][15])*(10**4))
            print("maksimum sehim :", maksimum_sehim)

            maksimum_moment = (p*l)/(4)
            print("maksimum moment :", maksimum_moment)

            maksimum_kesme = p/2

            zati_sehim = ((5*float(satir[0][1])*(9.81/1000)*(l*1000)
                          ** 4)/(384*E*(float(satir[0][15])*(10**4))))
            print("zati sehim :", zati_sehim)

            zati_moment = (float(satir[0][1])*9.81*(l**2))/(8)
            print("zati moment :", zati_moment)

            zati_kesme = float(satir[0][1])*l/2*9.81
            print("zati kesme :", zati_kesme)

            toplam_sehim = (zati_sehim + maksimum_sehim)
            print("toplam sehim", toplam_sehim)

            toplam_moment = (maksimum_moment+zati_moment)
            print("toplam moment :", toplam_moment)

            toplam_kesme = maksimum_kesme+zati_kesme
            print("toplam kesme :", toplam_kesme)

            aw = float(satir[0][9])*float(satir[0][4])
            cv1 = 1  # daha sonra formül eklenecek
            guvenli_kesme = 0.6*celik_sinifi*aw*cv1/1.5
            print("güvenli kesme :", guvenli_kesme)

            mg = yonetmelik9_2(l, celik_sinifi, satir)

            print("mg = ", mg)

            if ((mg >= toplam_moment) and ((l*1000/300) >= toplam_sehim) and (guvenli_kesme >= toplam_kesme)):
                uygun_mu = "UYGUN"
                print(uygun_mu)
            else:
                # kesit değiştirme yapılacak
                uygun_mu = "UYGUN DEĞİL"
                print(uygun_mu)

            return render_template("yontem_1.html", satir_liste=satir_liste, p=p, l=l, kesit=kesit, celik_sinifi=celik_sinifi, uygun_mu=uygun_mu)
        except:
            uygun_mu = "GEÇERLİ DEĞER GİRİLMEDİ"
            print(uygun_mu)
            return render_template("yontem_1.html", satir_liste=satir_liste, uygun_mu=uygun_mu)


# --2


@app.route("/yontem_2", methods=["POST", "GET"])
def yontem_2():
    try:
        print("LOCAL_VERİTABANI YÜKLENİYOR..")
        mydb = mysql.connector.connect(
            host="remotemysql.com",
            user="P0xYObZY55",
            password="3bT6PmoVEb",
            database="P0xYObZY55"
        )
        mycursor = mydb.cursor()
        print("LOCAL_VERİTABANI BAŞARILI ALINDI")

    except:
        print("WEB_VERİTABANI YÜKLENİYOR..")
        mydb = mysql.connector.connect(
            host="projecelikkiristasarim.mysql.pythonanywhere-services.com",
            user="projecelikkirist",
            password="8imtr4WtwXGaUp@",
            database="projecelikkirist$P0xYObZY55"
        )
        mycursor = mydb.cursor()
    print("WEB_VERİTABANI BAŞARILI ALINDI")

    E = 200000  # elastisite modulu (MPa)

    if request.method == "POST":
        try:
            mycursor.execute("SELECT * FROM a")
            satir = mycursor.fetchall()
            mydb.commit()

            p = request.form["p"]
            l = request.form["l"]
            celik_sinifi = request.form["celik_sinifi"]
            kesit_tipi = request.form["kesit_tipi"]
            yukleme_durumlari = request.form["yukleme_durumlari"]

            p = float(p)
            l = float(l)
            celik_sinifi = float(celik_sinifi)
            yukleme_durumlari = int(yukleme_durumlari)

            if yukleme_durumlari == 1:
                print("1_Basit Kiriş - Düzgün Yayılı Yük")
            elif yukleme_durumlari == 7:
                print("7_Basit Kiriş – Merkezde Noktasal Yük")
            elif yukleme_durumlari == 19:
                print("19_Konsol Kiriş – Düzgün Yayılı Yük")
            elif yukleme_durumlari == 22:
                print("22_Konsol Kiriş – Serbest Uçta Noktasal Yük")

            maksimum_moment = (p*l)/(4)
            print("maksimum moment :", maksimum_moment)

            wp_gerekli = maksimum_moment*1.67/celik_sinifi
            print("Wp gerekli : ", wp_gerekli)

            satir_dict = {}

            for i in range(len(satir)):

                if kesit_tipi in satir[i][0]:
                    satir_dict[satir[i][0]] = satir[i][17]
            print(satir_dict)

            while True:
                print("while girdi")

                fark = 100000
                kesit_2 = 0
                for x, y in satir_dict.items():
                    print(x, y)
                    if wp_gerekli <= float(y):
                        fark_temp = float(y)-wp_gerekli
                        if fark > fark_temp:
                            fark = fark_temp
                            kesit_2 = x

                if kesit_2 == 0:
                    uygun_mu = "VERİ TABANINDA UYGUN KESİT BULUNAMADI"
                    print(uygun_mu)
                    return render_template("yontem_2.html", uygun_mu=uygun_mu)

                print("kesit_2 :", kesit_2)

                mycursor.execute(
                    "SELECT * FROM a WHERE kesit='{}'".format(kesit_2))
                satir_2 = mycursor.fetchall()
                # print(satir)
                mydb.commit()

                maksimum_kesme = p/2

                zati_kesme = float(satir[0][1])*l/2*9.81
                print("zati kesme :", zati_kesme)

                toplam_kesme = maksimum_kesme+zati_kesme
                print("toplam kesme :", toplam_kesme)

                aw = float(satir[0][9])*float(satir[0][4])

                cv1 = 1  # daha sonra formül eklenecek

                guvenli_kesme = 0.6*celik_sinifi*aw*cv1/1.5
                print("güvenli kesme :", guvenli_kesme)

                zati_sehim = ((5*float(satir_2[0][1])*(9.81/1000)*(l*1000)**4)/(
                    384*E*(float(satir_2[0][15])*(10**4))))
                print("zati sehim :", zati_sehim)

                zati_moment = (float(satir_2[0][1])*9.81*(l**2))/(8)
                print("zati moment :", zati_moment)

                maksimum_sehim = (p*(l*1000)**3) / \
                    (48*E*float(satir_2[0][15])*(10**4))
                print("maksimum sehim :", maksimum_sehim)

                toplam_sehim = (zati_sehim + maksimum_sehim)
                print("toplam sehim :", toplam_sehim)

                toplam_moment = (maksimum_moment+zati_moment)
                print("toplam moment :", toplam_moment)

                mg = yonetmelik9_2(l, celik_sinifi, satir_2)
                print("guvenli egilme momenti dayanimi:", mg)

                if ((mg >= toplam_moment) and ((l*1000/300) >= toplam_sehim) and (guvenli_kesme >= toplam_kesme)):
                    uygun_mu = "UYGUN"
                    print(uygun_mu)
                    return render_template("yontem_2.html", kesitt=kesit_2, uygun_mu=uygun_mu)
                elif len(satir_dict) != 0:
                    satir_dict.pop(kesit_2)
                    print(satir_dict, "pop sonrası değer")
                    continue

                else:
                    uygun_mu = "VERİ TABANINDA UYGUN KESİT BULUNAMADI"
                    print(uygun_mu)
                    return render_template("yontem_2.html", uygun_mu=uygun_mu)

        except:
            uygun_mu = "GEÇERLİ DEĞER GİRİLMEDİ"
            print(uygun_mu)
            return render_template("yontem_2.html", uygun_mu=uygun_mu)


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port="5000")
