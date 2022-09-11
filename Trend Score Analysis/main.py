import json
import math
import matplotlib.pyplot as plt

y = []
for i in range(1, 101):
    y.append(i)


def ciz(grafik):
    plt.plot(y, grafik)
    plt.show()


def hesapla(data):
    with open(data, "r") as f:
        c = json.load(f)

    a = []

    for i in range(len(c)):
        a.append(c[i] * 25)

    peak = max(a)

    maxmagnitude = 200
    maxgrad = 25

    magnitudeweight = 0.75
    gradweight = 0.25


    grad = abs(a[99] - a[0])/4

    Score = pow(math.log10(peak) / math.log10(maxmagnitude), magnitudeweight) * pow(math.log10(grad) / math.log10(maxgrad),
                                                                               gradweight)
    print("Trend Score ***", round(Score.real * 100, 3), "***")
    ciz(a)

hesapla("data1.json")
hesapla("data2.json")
hesapla("data3.json")
hesapla("data4.json")
hesapla("data5.json")
hesapla("data6.json")
hesapla("data7.json")
hesapla("data8.json")
hesapla("data9.json")
hesapla("data10.json")
hesapla("data11.json")
hesapla("data12.json")