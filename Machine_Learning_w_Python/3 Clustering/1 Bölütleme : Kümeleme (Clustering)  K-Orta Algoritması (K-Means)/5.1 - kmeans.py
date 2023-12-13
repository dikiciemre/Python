

# K-Means kümeleme algoritması 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

veriler = pd.read_csv('musteriler.csv')

X = veriler.iloc[:,3:].values





from sklearn.cluster import KMeans

kmeans = KMeans ( n_clusters = 3, init = 'k-means++') # sklearn.cluster modülünden KMeans sınıfı kullanılarak bir K-Means kümeleme modeli oluşturulur. Bu model, 3 küme (n_clusters=3) kullanarak başlatılır ve "k-means++" yöntemi ile başlatılır.
kmeans.fit(X) # Oluşturulan K-Means modeli, fit yöntemi ile veri kümesine uyar.

print(kmeans.cluster_centers_) # Modelin küme merkezlerini göstermek için cluster_centers_ özelliği kullanılır ve bu merkezler ekrana yazdırılır.
sonuclar = []




for i in range(1,11):
    kmeans = KMeans (n_clusters = i, init='k-means++', random_state= 123)
    kmeans.fit(X)
    sonuclar.append(kmeans.inertia_) # Ardından, farklı küme sayıları için K-Means modeli oluşturulur ve her bir küme sayısı için çözünürlük değerleri (inertia) hesaplanır. Bu değerler "sonuclar" listesine eklenir.

plt.plot(range(1,11),sonuclar) # Birçok küme sayısı için inertia değerlerini içeren "sonuclar" listesi, grafiğe çizilir. Bu grafik, inertia'nın küme sayısına göre nasıl değiştiğini gösterir. Elbowed (dirsek) yöntemi ile optimal küme sayısını belirlemek için bu grafik kullanılabilir.
