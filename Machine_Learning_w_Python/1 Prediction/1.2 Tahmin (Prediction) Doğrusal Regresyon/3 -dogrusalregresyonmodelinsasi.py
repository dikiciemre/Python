

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


veriler = pd.read_csv('satislar.csv')

print(veriler)

aylar = veriler[['Aylar']]

satislar = veriler[['Satislar']]




#verilerin egitim ve test icin bolunmesi
from sklearn.model_selection import train_test_split

x_train, x_test,y_train,y_test = train_test_split(aylar,satislar,test_size=0.33, random_state=0)




#model insası(linear regression)
from sklearn.linear_model import LinearRegression

# sklearn.linear_model kütüphanesinden LinearRegression sınıfını içe aktarır ve bir doğrusal regresyon modeli (lr) oluştururuz. Daha sonra fit metodunu kullanarak modeli eğitiriz, yani eğitim veri setini kullanarak modelin katsayılarını öğreniriz.
lr=LinearRegression()
lr.fit(x_train,y_train)

# Eğitilen doğrusal regresyon modelini kullanarak test veri setindeki 'Aylar' özelliklerine dayalı olarak 'Satislar'ı tahmin ederiz. Tahmin sonuçları tahmin değişkenine kaydedilir.
tahmin = lr.predict(x_test)



