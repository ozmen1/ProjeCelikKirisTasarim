import mysql.connector
from flask import Flask, render_template, request
from functions import *
import time



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
            P = request.form["P"]
            L = request.form["L"]
            celik_sinifi = request.form["celik_sinifi"]
            kesit = request.form["kesit"]
            yukleme_durumlari = request.form["yukleme_durumlari"]
            yayili_yuk = request.form["w"]
            sehim_limiti = request.form["sehim_limit"]
            ilave_q = request.form["ilave_q"]
            Lb = request.form["Lb"]

            P = float(P)
            L = float(L)
            celik_sinifi = float(celik_sinifi)
            yukleme_durumlari = int(yukleme_durumlari)
            yayili_yuk = float(yayili_yuk)
            sehim_limiti = float(sehim_limiti)
            ilave_q = float(ilave_q)  # ----------------#### ## eklenecek
            Lb = float(Lb)
            if Lb == 0 or Lb > L:
                Lb = L
                print("Lb :", Lb)

            mycursor.execute("SELECT * FROM a WHERE kesit='{}'".format(kesit))
            satir = mycursor.fetchall()
            print(satir)
            mydb.commit()

            E = 200000  # elastisite modulu (MPa)
            maksimum_sehim=0
            maksimum_moment=0
            maksimum_kesme=0
            ilave_sehim=0

            if yukleme_durumlari == 1:
                print("1_Basit Kiriş - Düzgün Yayılı Yük")
                maksimum_sehim = (5 * yayili_yuk / 1000 * ((L * 1000) ** 4)) / \
                   (384 * E * float(satir[0][15]) * (10 ** 4))
                maksimum_moment = (yayili_yuk*(L**2))/(8)
                maksimum_kesme = (yayili_yuk*L)/(2)

            elif yukleme_durumlari == 7:
                print("7_Basit Kiriş – Merkezde Noktasal Yük")
                maksimum_sehim = (P*(L*1000)**3) / \
                    (48*E*float(satir[0][15])*(10**4))
                ilave_sehim=(5 * ilave_q / 1000 * ((L * 1000) ** 4)) / \
                   (384 * E * float(satir[0][15]) * (10 ** 4))
                maksimum_moment = (P*L)/(4)
                ilave_moment=(ilave_q*(L**2))/(8)
                maksimum_kesme = P/2
                ilave_kesme=(ilave_q*L)/(2)

            elif yukleme_durumlari == 19:
                print("19_Konsol Kiriş – Düzgün Yayılı Yük")
                maksimum_sehim = (yayili_yuk / 1000 * ((L * 1000)) ** 4) / \
                                 (8 * E * float(satir[0][15]) * (10 ** 4))
                maksimum_moment = (yayili_yuk * (L ** 2)) / (2)
                maksimum_kesme = (yayili_yuk * L)

            elif yukleme_durumlari == 22:
                print("22_Konsol Kiriş – Serbest Uçta Noktasal Yük")
                maksimum_sehim = (P * (L * 1000) ** 3) / \
                                 (3 * E * float(satir[0][15]) * (10 ** 4))
                ilave_sehim =(ilave_q / 1000 * ((L * 1000)) ** 4) / \
                                 (8 * E * float(satir[0][15]) * (10 ** 4))
                maksimum_moment = (P * L)
                ilave_moment = (ilave_q * (L ** 2)) / (2)
                maksimum_kesme = P
                ilave_kesme = (ilave_q * L)

            print("maksimum sehim :", maksimum_sehim)
            print("maksimum moment :", maksimum_moment)
            print("maksimum kesme :", maksimum_kesme)

            zati_sehim = ((5*float(satir[0][1])*(9.81/1000)*(L*1000)
                          ** 4)/(384*E*(float(satir[0][15])*(10**4))))
            print("zati sehim :", zati_sehim)

            zati_moment = (float(satir[0][1])*9.81*(L**2))/(8)
            print("zati moment :", zati_moment)

            zati_kesme = float(satir[0][1])*L/2*9.81
            print("zati kesme :", zati_kesme)

            print("ilave sehim :", ilave_sehim)
            print("ilave moment :", ilave_moment)
            print("ilave kesme :", ilave_kesme)


            toplam_sehim = (zati_sehim + maksimum_sehim+ilave_sehim)
            print("toplam sehim", toplam_sehim)

            toplam_moment = (maksimum_moment+zati_moment+ilave_moment)
            print("toplam moment :", toplam_moment)

            toplam_kesme = maksimum_kesme+zati_kesme+ilave_kesme
            print("toplam kesme :", toplam_kesme)

            Aw = float(satir[0][9])*float(satir[0][4])
            Cv1 = 1
            guvenli_kesme = 0.6*celik_sinifi*Aw*Cv1/1.5
            print("güvenli kesme :", guvenli_kesme)

            liste_s275 = ["HE 260 A", "HE 280 A", "HE 300 A"]
            liste_s355 = ["HE 180 A", "HE 200 A", "HE 220 A", "HE 240 A",
                          "HE 260 A", "HE 280 A", "HE 300 A", "HE 320 A", "HE 340 A"]

            if (celik_sinifi == 275 and (kesit in liste_s275)):
                print("kompakt olmayan-s275 listesinden aldı")
                Mn = yonetmelik9_3(celik_sinifi, satir, Lb)
            elif (celik_sinifi == 355 and (kesit in liste_s355)):
                print("kompakt olmayan-s355 listesinden aldı")
                Mn = yonetmelik9_3(celik_sinifi, satir, Lb)
            else:
                print("kompakt aldı")
                Mn = yonetmelik9_2(celik_sinifi, satir, Lb)

            Mg = Mn / 1.67    
            print("Mg = ", Mg)



            if ((Mg >= toplam_moment) and ((L*1000/sehim_limiti) >= toplam_sehim) and (guvenli_kesme >= toplam_kesme)):
                uygun_mu = "UYGUN"
                print(uygun_mu)
            else:
                # kesit değiştirme yapılacak
                uygun_mu = "UYGUN DEĞİL"
                print(uygun_mu)
            

            return render_template("yontem_1.html", satir_liste=satir_liste, P=P, L=L, kesit=kesit, celik_sinifi=celik_sinifi, yayili_yuk=yayili_yuk, uygun_mu=uygun_mu)
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

            P = request.form["P"]
            L = request.form["L"]
            celik_sinifi = request.form["celik_sinifi"]
            kesit_tipi = request.form["kesit_tipi"]
            yukleme_durumlari = request.form["yukleme_durumlari"]
            yayili_yuk = request.form["w"]
            sehim_limiti = request.form["sehim_limit"]
            ilave_q = request.form["ilave_q"]
            Lb = request.form["Lb"]

            P = float(P)
            L = float(L)
            celik_sinifi = float(celik_sinifi)
            yukleme_durumlari = int(yukleme_durumlari)
            yayili_yuk = float(yayili_yuk)
            sehim_limiti = float(sehim_limiti)
            ilave_q = float(ilave_q)  # eklenecek
            Lb = float(Lb)
            if Lb == 0 or Lb > L:
                Lb = L
                print("Lb :", Lb)

            if yukleme_durumlari == 1:
                print("1_Basit Kiriş - Düzgün Yayılı Yük")
                maksimum_moment = (yayili_yuk*(L**2))/(8)
            elif yukleme_durumlari == 7:
                print("7_Basit Kiriş – Merkezde Noktasal Yük")
                maksimum_moment = (P*L)/(4)
                ilave_moment=(ilave_q*(L**2))/(8)
            elif yukleme_durumlari == 19:
                print("19_Konsol Kiriş – Düzgün Yayılı Yük")
                maksimum_moment = (yayili_yuk*(L**2))/(2)
            elif yukleme_durumlari == 22:
                print("22_Konsol Kiriş – Serbest Uçta Noktasal Yük")
                maksimum_moment = (P*L)
                ilave_moment=(ilave_q*(L**2))/(2)

            toplam_moment=maksimum_moment+ilave_moment
            print("maksimum moment :", maksimum_moment)
            print("ilave moment :", ilave_moment)

            Wp_gerekli = toplam_moment*1.67/celik_sinifi
            print("Wp gerekli : ", Wp_gerekli)

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
                    if Wp_gerekli <= float(y):
                        fark_temp = float(y)-Wp_gerekli
                        if fark > fark_temp:
                            fark = fark_temp
                            kesit_2 = x

                if kesit_2 == 0:
                    uygun_mu = "VERİ TABANINDA UYGUN KESİT BULUNAMADI"
                    print(uygun_mu)
                    return render_template("yontem_2.html", uygun_mu=uygun_mu)

                mycursor.execute(
                    "SELECT * FROM a WHERE kesit='{}'".format(kesit_2))
                satir_2 = mycursor.fetchall()
                # print(satir)
                mydb.commit()

                if yukleme_durumlari == 1:
                    print("1_Basit Kiriş - Düzgün Yayılı Yük")
                    maksimum_sehim = (5 * yayili_yuk/1000 * ((L*1000) ** 4)) / \
                        (384 * E * float(satir_2[0][15]) * (10 ** 4))
                    maksimum_moment = (yayili_yuk * (L ** 2)) / (8)
                    maksimum_kesme = (yayili_yuk * L) / (2)

                elif yukleme_durumlari == 7:
                    print("7_Basit Kiriş – Merkezde Noktasal Yük")
                    maksimum_sehim = (P * (L * 1000) ** 3) / \
                        (48 * E * float(satir_2[0][15]) * (10 ** 4))
                    maksimum_moment = (P * L) / (4)
                    maksimum_kesme = P / 2
                    ilave_sehim=(5 * ilave_q/1000 * ((L*1000) ** 4)) / \
                        (384 * E * float(satir_2[0][15]) * (10 ** 4))
                    ilave_moment=(ilave_q * (L ** 2)) / (8)
                    ilave_kesme = (ilave_q * L) / (2)

                elif yukleme_durumlari == 19:
                    print("19_Konsol Kiriş – Düzgün Yayılı Yük")
                    maksimum_sehim = (yayili_yuk/1000 * ((L*1000) ** 4)) / \
                        (8 * E * float(satir_2[0][15]) * (10 ** 4))
                    maksimum_moment = (yayili_yuk * (L ** 2)) / (2)
                    maksimum_kesme = (yayili_yuk * L)

                elif yukleme_durumlari == 22:
                    print("22_Konsol Kiriş – Serbest Uçta Noktasal Yük")
                    maksimum_sehim = (P * (L * 1000) ** 3) / \
                        (3 * E * float(satir_2[0][15]) * (10 ** 4))
                    maksimum_moment = (P * L)
                    maksimum_kesme = P
                    ilave_sehim = (ilave_q/1000 * ((L*1000) ** 4)) / \
                        (8 * E * float(satir_2[0][15]) * (10 ** 4))
                    ilave_moment = (ilave_q * (L ** 2)) / (2)
                    ilave_kesme = (ilave_q * L)

                print("maksimum sehim :", maksimum_sehim)
                print("maksimum moment :", maksimum_moment)
                print("maksimum kesme :", maksimum_kesme)

                zati_kesme = float(satir_2[0][1])*L/2*9.81
                print("zati kesme :", zati_kesme)

                toplam_kesme = maksimum_kesme+zati_kesme+ilave_kesme
                print("toplam kesme :", toplam_kesme)

                Aw = float(satir_2[0][9])*float(satir_2[0][4])
                Cv1 = 1
                guvenli_kesme = 0.6*celik_sinifi*Aw*Cv1/1.5
                print("güvenli kesme :", guvenli_kesme)

                zati_sehim = (5*float(satir_2[0][1])*(9.81/1000)*(L*1000)**4)/(
                    384*E*(float(satir_2[0][15])*(10**4)))
                print("zati sehim :", zati_sehim)

                zati_moment = (float(satir_2[0][1])*9.81*(L**2))/(8)
                print("zati moment :", zati_moment)

                toplam_sehim = (zati_sehim + maksimum_sehim+ilave_sehim)
                print("toplam sehim :", toplam_sehim)

                toplam_moment = (maksimum_moment+zati_moment+ilave_moment)
                print("toplam moment :", toplam_moment)

                liste_s275 = ["HE 260 A", "HE 280 A", "HE 300 A"]
                liste_s355 = ["HE 180 A", "HE 200 A", "HE 220 A", "HE 240 A",
                              "HE 260 A", "HE 280 A", "HE 300 A", "HE 320 A", "HE 340 A"]

                if (celik_sinifi == 275 and (kesit_2 in liste_s275)):
                    print("kompakt olmayan-s275 listesinden aldı")
                    Mn = yonetmelik9_3(celik_sinifi, satir_2, Lb)
                elif (celik_sinifi == 355 and (kesit_2 in liste_s355)):
                    print("kompakt olmayan-s355 listesinden aldı")
                    Mn = yonetmelik9_3(celik_sinifi, satir_2, Lb)
                else:
                    print("kompakt aldı")
                    Mn = yonetmelik9_2(celik_sinifi, satir_2, Lb)

                Mg = Mn / 1.67
                print("Mg = ", Mg)

                if ((Mg >= toplam_moment) and ((L*1000/sehim_limiti) >= toplam_sehim) and (guvenli_kesme >= toplam_kesme)):
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
