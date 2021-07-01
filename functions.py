import math

def yonetmelik9_2(celik_sinifi, satir, Lb):
    E = 200000
    Mp = celik_sinifi * float(satir[0][17])
    Lp = (float(satir[0][23]) *
          (1.76 * (math.sqrt(E / celik_sinifi)))) / 100
    print("Lp :", Lp)

    if Lb <= Lp:
        Mn = Mp
        print("Lb <= Lp: durumu oldu  ", Mn)
    else:
        d = float(satir[0][2])
        print("d: ", d)
        tf = float(satir[0][5])
        print("tf: ", tf)
        bf = float(satir[0][3])
        print("bf: ", bf)
        h = float(satir[0][9])
        print("h: ", h)
        tw = float(satir[0][4])
        print("tw: ", tw)
        Wex = float(satir[0][16])
        print("Wex: ", Wex)
        J = float(satir[0][25])
        print("J: ", J)
        Iy = float(satir[0][15])
        print("Iy: ", Iy)
        h0 = d - tf
        print("h0: ", h0)
        its = bf/math.sqrt(12*(1+h*tw/(6*bf*tf)))/10
        print("its: ", its)
        Lr = (1.95 * its * (E / 0.7 / celik_sinifi) * math.sqrt((J / (Wex * h0/10)) + math.sqrt(
            math.pow((J / (Wex * h0/10)), 2) + 6.76 * math.pow((0.7 * celik_sinifi / E), 2)))) / 100
        print("Lr: ", Lr)
        if Lp < Lb and Lb <= Lr:
            Mn = min(1 * (Mp - (Mp - 0.7 * celik_sinifi * Wex)
                      * ((Lb - Lp) / (Lr - Lp))) , Mp)
            print("Lp < Lb <=Lr: durumu oldu", Mn)
        else:
            Fcr = (1 * (math.pi ** 2) * E) / math.pow((Lb*100 / its), 2)*math.sqrt(1 + 0.078 * J
                                                                                   / (Wex * h0/10) * math.pow((Lb*100 / its), 2))
            Mn = min(Fcr * Wex, Mp)
            print("Lb > Lr: durumu oldu", Mn)
    if Mn <= Mp:
        M = Mn
    else:
        M = Mp
    print("Mn = ", M)
    return(M)


def yonetmelik9_3(celik_sinifi, satir, Lb):
    E = 200000
    Mp = celik_sinifi * float(satir[0][17])
    print("Mp = ", Mp)
    bf = float(satir[0][3])
    tf = float(satir[0][5])
    Nf = (bf/2) / tf
    Npf = 0.38 * math.sqrt(E/celik_sinifi)
    Nrf = 1.00 * math.sqrt(E/celik_sinifi)
    Mn1 = yonetmelik9_2(celik_sinifi, satir, Lb)
    print("Yanal burulmalı burkulma sınır durumu, Mn1 =", Mn1)
    Mn2 = Mp-(Mp-0.7*celik_sinifi*float(satir[0][16]))*((Nf-Npf)/(Nrf-Npf))
    print("Yerel burkulma sınır durumu, Mn2 =", Mn2)
    if Mn2 <= Mn1:
        M = Mn2
    else:
        M = Mn1
    print("Mn = ", M)
    return(M)
