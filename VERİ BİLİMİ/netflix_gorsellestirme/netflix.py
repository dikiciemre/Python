#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 12:53:38 2023

@author: emredikici
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


netflix = pd.read_csv("netflix_titles.csv")
print( netflix.head())

shape_of_netflix = netflix.shape

null = netflix.isnull().sum()


unique = netflix.nunique() # farklı her bir veriyi gösterir

data = netflix.copy() # netflix verilerinin yedeiğini aldım

data = data.dropna() # eksik verileri temizledim doldurmak istemedim






# Movie ve TV Show kategorilerinde kaçar tane eser olduğunu gösterir
"""
# 'type' sütununu inceleyin ve sayımları alın
type_counts = netflix['type'].value_counts()

# Sayıları içeren bir çubuk grafik çizin
plt.figure(figsize=(5, 5))
sns.barplot(x=type_counts.index, y=type_counts.values)
plt.title("Tür")
plt.show()
"""






# her raytingde toplam kaç adet eser olduğunu söyler
"""
# rating türlerini sıralar
rating_counts = netflix['rating'].value_counts()

# Sayıları içeren bir çubuk grafik çizin
plt.figure(figsize=(13, 13))
sns.barplot(x=rating_counts.index, y=rating_counts.values)
plt.title("Rating")
plt.show()
"""








# her bir rayting çeşitinde kaç adet film ve ya tv show olduğunu söyler
"""
# rating türlerini sıralar
rating_counts = netflix['rating']
type_counts = netflix['type']


# Sayıları içeren bir çubuk grafik çizin
plt.figure(figsize=(10, 8))
sns.countplot(x=rating_counts, hue=type_counts )
plt.title("Rating")
plt.show()
"""






# netflix veri setinin ilk 100 satırı alındı(çok uzun olduğu için)
# bu kodda her bir yılda kaç adet tv show kaç adet movie çıktığını söyler
"""
ilk_100_satir = netflix.head(100)

year_counts = ilk_100_satir["release_year"]
type_counts = ilk_100_satir['type']


plt.figure(figsize=(13,13))
sns.countplot(x=year_counts, hue=type_counts)
plt.title("Year İnfo")
plt.show()
"""








# pasta diliminde kaç adet movie kaç adet tv show olduğunu yüzdelik halde gösterir
"""
type_counts = netflix['type'].value_counts()

plt.figure(figsize=(6, 6))  # Grafiğin boyutunu ayarlayabilirsiniz
MyExplode = [0,0.1] # pasta dilimlerini biribirinden ayırır
MyColors = ["#713ABE","#F4E869"] # dilim renklerini belirtir
plt.rcParams["figure.figsize"]=(9,9)

plt.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', startangle=90,explode = MyExplode, shadow=True, colors = MyColors)  # autopct ile yüzdelikleri gösterir, startangle ile başlangıç açısını ayarlar
plt.title('Örnek Pasta Grafiği',fontsize=25)

# Grafiği gösterin
plt.show()
"""







# netflix veri setinden ilk 100 verisi için hangi reyting türünde ne kadar eser var onlar bastırıldı
"""
ilk_100_satir = netflix.head(100)


rayting_counts = ilk_100_satir['rating'].value_counts()

plt.figure(figsize=(15, 15))  # Grafiğin boyutunu ayarlayabilirsiniz
MyColors = ["#713ABE","#F4E869","pink"] # dilim renklerini belirtir
plt.rcParams["figure.figsize"]=(20,20)

plt.pie(rayting_counts, labels=rayting_counts.index, autopct='%1.1f%%', startangle=90, shadow=True, colors = MyColors)  # autopct ile yüzdelikleri gösterir, startangle ile başlangıç açısını ayarlar
plt.title('Örnek Pasta Grafiği',fontsize=25)

# Grafiği gösterin
plt.show()
"""

















