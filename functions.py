import math

def yonetmelik9_2(l,celik_sinifi,satir):
    mp = celik_sinifi * float(satir[0][17])
    mg = mp / 1.67
    print("guvenli egilme momenti dayanimi :", mg)

    lp = (float(satir[0][23]) *
          (1.76 * (math.sqrt(200000 / celik_sinifi)))) / 100
    print("lp :", lp)

    if l <= lp:
        mn = mp
        print("l <= lp: durumu oldu  ", mn)
    else:
        d = float(satir[0][9])
        print("d: ", d)
        tf = float(satir[0][5])
        print("tf: ", tf)
        wex = float(satir[0][16])
        print("wex: ", wex)
        j = float(satir[0][25])
        print("j: ", j)
        iy = float(satir[0][15])
        print("iy: ", iy)
        h0 = d - tf
        print("h0: ", h0)
        cw = (iy * math.pow(h0, 2)) / 4
        print("cw: ", cw)

        its = math.sqrt((math.sqrt(iy * cw) / wex))
        print("its: ", its)
        lr = (1.95 * its * (200000 / 0.7 * celik_sinifi) * math.sqrt((j / (wex * h0)) + math.sqrt(
            math.pow((j / (wex * h0)), 2) + 6.76 * math.pow((0.7 * celik_sinifi / 200000), 2)))) / 100
        print("lr: ", lr)

        if lp < l <= lr:
            mn = (1 * (mp - (mp - 0.7 * celik_sinifi * wex) * ((l - lp) / (lr - lp)))) / 1.67
            print("lp < l <=lr: durumu oldu", mn)

        elif l > lr:
            fcr = (1 * (math.pi ** 2) * 200000) / (math.pow(l / its), 2) * \
                  (math.sqrt(1 + 0.78 * (j / (wex * h0)) * math.pow((l / its), 2)))
            mn = (fcr * wex) / 1.67
            print("l>lr: durumu oldu", mn)

    if mn <= mp:
        m = mn
    else:
        m = mp

    return(m)