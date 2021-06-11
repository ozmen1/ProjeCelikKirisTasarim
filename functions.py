import math

def yonetmelik9_2(l,celik_sinifi,satir):
    E=200000
    mp = celik_sinifi * float(satir[0][17])
    lp = (float(satir[0][23]) *
          (1.76 * (math.sqrt(E / celik_sinifi)))) / 100
    print("lp :", lp)

    if l <= lp:
        mn = mp
        print("l <= lp: durumu oldu  ", mn)
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
        wex = float(satir[0][16])
        print("wex: ", wex)
        j = float(satir[0][25])
        print("j: ", j)
        iy = float(satir[0][15])
        print("iy: ", iy)
        h0 = d - tf
        print("h0: ", h0)
        its = bf/math.sqrt(12*(1+h*tw/(6*bf*tf)))/10
        print("its: ", its)
        lr = (1.95 * its * (E / 0.7 / celik_sinifi) * math.sqrt((j / (wex * h0/10)) + math.sqrt(
            math.pow((j / (wex * h0/10)), 2) + 6.76 * math.pow((0.7 * celik_sinifi / E), 2)))) / 100
        print("lr: ", lr)

#        if lp < l <= lr:
        if lp < l  and l <= lr:
            mn = 1 * (mp - (mp - 0.7 * celik_sinifi * wex) * ((l - lp) / (lr - lp)))
            print("lp < l <=lr: durumu oldu", mn)
        else:
            fcr = (1 * (math.pi ** 2) * E) / math.pow((l*100 / its),2)*math.sqrt(1 + 0.078 * j
                / (wex * h0/10) * math.pow((l*100 / its), 2))
            mn = fcr * wex
            print("l>lr: durumu oldu", mn)

    if mn <= mp:
        m = mn
    else:
        m = mp

    mg = m / 1.67

    print("mn = ",m)
    print("guvenli egilme momenti dayanimi :", mg)

    return(mg)