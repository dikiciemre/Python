#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 19:04:05 2023

@author: emredikici
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Veri setini oluşturun
veri = pd.DataFrame({
    'Marka': ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'Volkswagen', 'BMW', 'Hyundai', 'Nissan', 'Mercedes', 'Audi'],
    'Renk': ['Kırmızı', 'Mavi', 'Siyah', 'Beyaz', 'Gri', 'Siyah', 'Beyaz', 'Kırmızı', 'Siyah', 'Mavi'],
    'Yaş': [3, 5, 2, 1, 4, 2, 6, 4, 3, 2],
    'Hız': [160, 140, 170, 180, 150, 200, 130, 160, 190, 210]
})



data = pd.DataFrame(veri)
print(data)


median_of_age = data["Yaş"].mean()
print(median_of_age)




#           ********ÇİZGİ GRAFİĞİ********

# yıldız sembolü ile hangi araba kaç hız yapmış onu gösteriyor.
# 'type' sütununu inceleyin ve sayımları alın
"""
Speed_counts = data['Hız']
Brand_counts = data['Marka'].value_counts()

xpoints = Brand_counts.index
ypoints = Speed_counts

plt.figure(figsize=(13,13))
plt.plot(xpoints, ypoints,'*')
plt.show()
"""









# yuvarlak sembolü ile hangi araba kaç hız yapmış onu gösteriyor.
# 'type' sütununu inceleyin ve sayımları alın

Speed_counts = data['Hız']
Brand_counts = data['Marka'].value_counts()

xpoints = Brand_counts.index
ypoints = Speed_counts

plt.figure(figsize=(13,13))
plt.plot(xpoints, ypoints,marker="o")
plt.show()










#ms verilen şeklin kalın lığını , mec şeklin çerçeve rengini belirler
# mfc = 'r' ise şeklin rengini değiştirir( burada kırmızı )
"""
Speed_counts = data['Hız']
Brand_counts = data['Marka'].value_counts()

xpoints = Brand_counts.index
ypoints = Speed_counts

plt.figure(figsize=(13,13))
plt.plot(xpoints, ypoints,marker="o",ms = 20, mec = 'r')
plt.show()

"""







#linewidth çizgiyi kalınlaştırır
#grid grafiğe ızgara ekler özellikler ile grid değiştirilir(renk kalınlık vs)
"""
age_of_cars = data['Yaş']
Brand = data['Marka'].value_counts()

x = Brand.index
y = age_of_cars


plt.figure(figsize=(13,13))
plt.plot(x, y,color = 'r',linewidth = '7.5',)

plt.title("Marka-Yaş Grafiği")
plt.xlabel("Marka")
plt.ylabel("Yaş")
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
plt.show()
"""








#scatter ile nokta grafiği yapıldı
"""
age_of_cars = data['Yaş']
Brand = data['Marka'].value_counts()

x = Brand.index
y = age_of_cars


plt.figure(figsize=(13,13))
plt.scatter(x, y)

plt.title("Marka-Yaş Grafiği")
plt.xlabel("Marka")
plt.ylabel("Yaş")
plt.show()
"""















#        *******SÜTUN GRAFİĞİ*******


#plt.bar ile sutün grafiği çizildi
#color ile sütunlara renk verildi
"""
age_of_cars = data['Yaş']
Brand = data['Marka'].value_counts()

x = Brand.index
y = age_of_cars


plt.figure(figsize=(13,13))
plt.bar(x,y, color = "red")


plt.title("Marka-Yaş Grafiği")
plt.xlabel("Marka")
plt.ylabel("Yaş")
plt.show()
"""








# Markaların yapmış olduğu hızlar sütun grafiğine döküldü ve hızları üstüne  yazıldı
"""
speed = data["Hız"]
Brand = data["Marka"].value_counts()

x = Brand.index
y = speed


plt.figure(figsize=(13,13))


#hızları üstüne yazan kod (for döngüsü)
for i, v in enumerate(y):
    plt.text(i, v, str(v), ha='center', va='bottom', fontsize=12)


plt.title("Marka-Hız Grafiği")
plt.xlabel("Marka")
plt.ylabel("Hız")

plt.bar(x,y)
"""














#        ******* PASTA GRAFİĞİ *******






# marka-hız değerleri ile bir pasta grafiği oluşturuldu.
"""
age_of_cars = data['Yaş']
Brand = data['Marka'].value_counts()

y = Brand.index
x = age_of_cars

plt.figure(figsize=(9, 9))  # Grafiğin boyutunu ayarlayabilirsiniz
MyExplode = [0,0.1,0,0,0.1,0,0,0.1,0,0] # pasta dilimlerini biribirinden ayırır
MyColors = ["#713ABE","#F4E869"] # dilim renklerini belirtir
plt.rcParams["figure.figsize"]=(9,9)

plt.pie(x, labels=y, autopct='%1.1f%%', startangle=90,explode = MyExplode, shadow=True, colors = MyColors)  # autopct ile yüzdelikleri gösterir, startangle ile başlangıç açısını ayarlar
plt.title('Marka Hız Pasta Grafiği',fontsize=25)

# Grafiği gösterin
plt.show()
"""













