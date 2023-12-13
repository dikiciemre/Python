

# K-Means ve Hiyerarşik Kümeleme yöntemi


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

veriler = pd.read_csv('musteriler.csv')

X = veriler.iloc[:,3:].values




#K -Means Kümeleme Bölümü:

from sklearn.cluster import KMeans

kmeans = KMeans ( n_clusters = 3, init = 'k-means++') # Veri çerçevesinden sadece 3. sütun (indeks 2) ve sonraki sütunlar seçilerek "X" adlı bir veri kümesi oluşturuluyor.
kmeans.fit(X)

# K-Means kümeleme algoritması kullanılıyor. Önce 3 küme için bir K-Means modeli oluşturuluyor ve bu model veri kümesine uyarılıyor. Ardından, bu modelin küme merkezleri kmeans.cluster_centers_ ile yazdırılıyor.
print(kmeans.cluster_centers_)
sonuclar = []

for i in range(1,11):
    kmeans = KMeans (n_clusters = i, init='k-means++', random_state= 123)
    kmeans.fit(X)
    sonuclar.append(kmeans.inertia_)


# Farklı küme sayıları için K-Means modelinin inertia (küme içi varyans) değerleri hesaplanarak, bu değerler sonuclar listesine ekleniyor ve bu değerlerin grafiği çiziliyor.
plt.plot(range(1,11),sonuclar)
plt.show()



# Bir sonraki adımda, 4 küme için yeni bir K-Means modeli oluşturuluyor ve bu model ile veri kümesi üzerinde tahminler yapılıyor (Y_tahmin). Tahmin sonuçlarına göre veri noktaları farklı renklerde noktalarla görselleştiriliyor.
kmeans = KMeans (n_clusters = 4, init='k-means++', random_state= 123)
Y_tahmin= kmeans.fit_predict(X)
print(Y_tahmin)  
plt.scatter(X[Y_tahmin==0,0],X[Y_tahmin==0,1],s=100, c='red')
plt.scatter(X[Y_tahmin==1,0],X[Y_tahmin==1,1],s=100, c='blue')
plt.scatter(X[Y_tahmin==2,0],X[Y_tahmin==2,1],s=100, c='green')
plt.scatter(X[Y_tahmin==3,0],X[Y_tahmin==3,1],s=100, c='yellow')
plt.title('KMeans')
plt.show()






#HC

from sklearn.cluster import AgglomerativeClustering

ac = AgglomerativeClustering(n_clusters=4, affinity='euclidean', linkage='ward') # Agglomerative Clustering yöntemi kullanılarak bir Hiyerarşik Kümeleme modeli oluşturuluyor. Bu model, 4 küme için oluşturuluyor ve "euclidean" uzaklık metriği ve "ward" bağlama yöntemi kullanılıyor.
Y_tahmin = ac.fit_predict(X) # Bu Hiyerarşik Kümeleme modeli ile veri kümesi üzerinde tahminler yapılıyor ve tahmin sonuçları Y_tahmin adlı bir değişkene atanıyor.
print(Y_tahmin)


# Tahmin sonuçlarına göre veri noktaları farklı renklerde noktalarla görselleştiriliyor.
plt.scatter(X[Y_tahmin==0,0],X[Y_tahmin==0,1],s=100, c='red')
plt.scatter(X[Y_tahmin==1,0],X[Y_tahmin==1,1],s=100, c='blue')
plt.scatter(X[Y_tahmin==2,0],X[Y_tahmin==2,1],s=100, c='green')
plt.scatter(X[Y_tahmin==3,0],X[Y_tahmin==3,1],s=100, c='yellow')
plt.title('HC')
plt.show()


# Son olarak, dendrogram (ağaç diyagramı) oluşturmak için SciPy kütüphanesinin scipy.cluster.hierarchy modülü kullanılıyor ve bu dendrogram görselleştiriliyor.
import scipy.cluster.hierarchy as sch
dendrogram = sch.dendrogram(sch.linkage(X, method='ward'))
plt.show()





