import math

def yonetmelik9_2(l,celik_sinifi,satir):
    E=200000
    Mp = celik_sinifi * float(satir[0][17])
    Lp = (float(satir[0][23]) *
          (1.76 * (math.sqrt(E / celik_sinifi)))) / 100
    print("Lp :", Lp)

    if l <= Lp:
        Mn = Mp
        print("L <= Lp: durumu oldu  ", Mn)
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

#        if Lp < l <= Lr:
        if Lp < l  and l <= Lr:
            Mn = 1 * (Mp - (Mp - 0.7 * celik_sinifi * Wex) * ((l - Lp) / (Lr - Lp)))
            print("Lp < L <=Lr: durumu oldu", Mn)
        else:
            Fcr = (1 * (math.pi ** 2) * E) / math.pow((l*100 / its),2)*math.sqrt(1 + 0.078 * J
                / (Wex * h0/10) * math.pow((l*100 / its), 2))
            Mn = Fcr * Wex
            print("L > Lr: durumu oldu", Mn)

    if Mn <= Mp:
        M = Mn
    else:
        M = Mp

    mg = M / 1.67

    print("Mn = ",M)
    print("guvenli egilme momenti dayanimi :", mg)

    return(mg)