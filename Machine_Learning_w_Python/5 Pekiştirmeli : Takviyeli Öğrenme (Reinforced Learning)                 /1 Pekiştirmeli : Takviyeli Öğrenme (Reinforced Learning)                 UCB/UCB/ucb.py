
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

veriler = pd.read_csv('Ads_CTR_Optimisation.csv')

import math

#UCB
N = 10000 # 10.000 tıklama
d = 10  # Toplam reklam seçeneği sayısını temsil eder. Bu durumda, 10 farklı reklam seçeneği vardır.
oduller = [0] * d #iHer reklamın toplam ödülünü tutan bir liste oluşturulur. İlk başta her reklamın ödülü 0 olarak başlar.


tiklamalar = [0] * d #o ana kadarki tıklamalar
toplam = 0 # Toplam ödülü izlemek için kullanılan bir değişkendir.
secilenler = [] #  Her dönemde seçilen reklamın endeksini izlemek için kullanılan bir liste oluşturulur.


for n in range(1,N): # for döngüsü, 1'den N'e kadar olan dönemleri temsil eder ve her dönemde bir reklam seçilir.
    ad = 0 #seçilen ilan
    max_ucb = 0
    for i in range(0,d):
        if(tiklamalar[i] > 0):
            ortalama = oduller[i] / tiklamalar[i]
            delta = math.sqrt(3/2* math.log(n)/tiklamalar[i])
            ucb = ortalama + delta
        else:
            ucb = N*10
        if max_ucb < ucb: #max'tan büyük bir ucb çıktı
            max_ucb = ucb
            ad = i  
            
    secilenler.append(ad) # En yüksek UCB değerine sahip reklam seçilir ve secilenler listesine eklenir.
    tiklamalar[ad] = tiklamalar[ad]+ 1 # Seçilen reklamın tıklama sayısı ve ödülü güncellenir.
    odul = veriler.values[n,ad] # verilerdeki n. satır = 1 ise odul 1
    oduller[ad] = oduller[ad]+ odul
    toplam = toplam + odul # Toplam ödül, her dönemdeki ödülle güncellenir.
    
print('Toplam Odul:')   
print(toplam)

plt.hist(secilenler) # plt.hist(secilenler) kullanarak, her reklamın kaç kez seçildiğini gösteren bir histogram oluşturulur.
plt.show()


