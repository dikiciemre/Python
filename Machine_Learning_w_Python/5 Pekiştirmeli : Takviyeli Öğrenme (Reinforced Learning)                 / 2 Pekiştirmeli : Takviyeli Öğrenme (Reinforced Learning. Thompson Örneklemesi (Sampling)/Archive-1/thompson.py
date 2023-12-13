
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

veriler = pd.read_csv('Ads_CTR_Optimisation.csv')



import random
#UCB
N = 10000 # Toplam simülasyon dönemi sayısını temsil eder. Bu durumda, 10.000 dönem boyunca simülasyon yapılır.
d = 10  # Toplam reklam seçeneği sayısını temsil eder. Bu durumda, 10 farklı reklam seçeneği vardır.


toplam = 0 # toplam odul
secilenler = [] # : Her dönemde seçilen reklamın endeksini izlemek için kullanılan bir liste oluşturulur.

# Her reklamın kazanma ve kaybetme sayılarını izlemek için kullanılan listeler oluşturulur.
birler = [0] * d
sifirlar = [0] * d


#for döngüsü, 1'den N'e kadar olan dönemleri temsil eder ve her dönemde bir reklam seçilir.
for n in range(1,N):
    ad = 0 #seçilen ilan
    max_th = 0
    for i in range(0,d):
        rasbeta = random.betavariate ( birler[i] + 1 , sifirlar[i] +1) # Her reklam için Beta dağılımı kullanılarak rastgele bir örnek çekilir. Bu örnek, her reklamın tahmini kazanma olasılığını günceller.
        if rasbeta > max_th:
            max_th = rasbeta
            ad = i
    secilenler.append(ad) # En yüksek örnekleme değerine sahip reklam seçilir ve secilenler listesine eklenir.
    odul = veriler.values[n,ad] # verilerdeki n. satır = 1 ise odul 1
    
    # Reklamın sonucu (kazanma veya kaybetme) gözlemlenir ve kazanma durumunda birler, kaybetme durumunda sifirlar güncellenir.
    if odul == 1:
        birler[ad] = birler[ad]+1
    else :
        sifirlar[ad] = sifirlar[ad] + 1
    toplam = toplam + odul
    
print('Toplam Odul:')   
print(toplam)

plt.hist(secilenler) # plt.hist(secilenler) kullanarak, her reklamın kaç kez seçildiğini gösteren bir histogram oluşturulur.
plt.show()







