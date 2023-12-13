
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

veriler = pd.read_csv('veriler.csv')


#encoder: Kategorik -> Numeric
ulke = veriler.iloc[:,0:1].values

Yas = veriler.iloc[:, 1:4].values



from sklearn import preprocessing

le = preprocessing.LabelEncoder()

ulke[:,0] = le.fit_transform(veriler.iloc[:,0]) # LabelEncoder kullanarak Ulke sütununu sayısal değerlere dönüştürürsünüz.


# Ardından, One-Hot Encoding kullanarak Ulke sütununu dönüştürürsünüz. Bu, çoklu sütunlu bir dizi (ulke) elde etmenizi sağlar.
ohe = preprocessing.OneHotEncoder()
ulke = ohe.fit_transform(ulke).toarray()
print(ulke)

#encoder: Kategorik -> Numeric # Veri çerçevesinden son sütunu (Cinsiyet) alırsınız ve bu sütunu c adlı bir NumPy dizisine atarsınız.
c = veriler.iloc[:,-1:].values
print(c)




from sklearn import preprocessing

le = preprocessing.LabelEncoder()

# LabelEncoder kullanarak Cinsiyet sütununu sayısal değerlere dönüştürürsünüz.
c[:,-1] = le.fit_transform(veriler.iloc[:,-1])

print(c)

# Ardından, One-Hot Encoding kullanarak Cinsiyet sütununu dönüştürürsünüz. Bu, çoklu sütunlu bir dizi (c) elde etmenizi sağlar.
ohe = preprocessing.OneHotEncoder()
c = ohe.fit_transform(c).toarray()
print(c)



#numpy dizileri dataframe donusumu # NumPy dizilerini Pandas DataFrame'lerine dönüştürerek, verileri daha iyi işleyebilir bir formata getirirsiniz.
sonuc = pd.DataFrame(data=ulke, index = range(22), columns = ['fr','tr','us'])
print(sonuc)

sonuc2 = pd.DataFrame(data=Yas, index = range(22), columns = ['boy','kilo','yas'])
print(sonuc2)

cinsiyet = veriler.iloc[:,-1].values
print(cinsiyet)

sonuc3 = pd.DataFrame(data = c[:,:1], index = range(22), columns = ['cinsiyet'])
print(sonuc3)



#dataframe birlestirme islemi
s=pd.concat([sonuc,sonuc2], axis=1)
print(s)

s2=pd.concat([s,sonuc3], axis=1)
print(s2)




# Veri setini eğitim ve test setlerine bölersiniz. Özellikler (s) ve hedef değişken (sonuc3) olarak ayrılır. Veri setinin %33'ü test için ayrılmıştır. Bu bölünmüş veri setleri, makine öğrenimi modellerinin eğitilmesi ve test edilmesi için kullanılır.
#verilerin egitim ve test icin bolunmesi
from sklearn.model_selection import train_test_split

x_train, x_test,y_train,y_test = train_test_split(s,sonuc3,test_size=0.33, random_state=0)




# sklearn.linear_model kütüphanesinden LinearRegression sınıfını içe aktarır ve bir doğrusal regresyon modeli (regressor) oluştururuz. Daha sonra fit metodunu kullanarak modeli eğitiriz, yani eğitim veri setini kullanarak modelin katsayılarını öğreniriz.
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)


# Eğitilen doğrusal regresyon modelini kullanarak test veri setindeki özelliklere (x_test) dayalı olarak tahminler yaparız. Tahmin sonuçları y_pred değişkenine kaydedilir.
y_pred = regressor.predict(x_test)


# İlk DataFrame (s2) içerisinden 'boy' sütununu ayrıştırırız ve bunu bir NumPy dizisi olan boy değişkenine atarız.
boy = s2.iloc[:,3:4].values
print(boy)

# lk DataFrame'den ('s2') bağımsız değişkenler ve bağımlı değişken ayrıştırılır ve sonunda birleştirilerek 'veri' adlı yeni bir DataFrame elde edilir.
sol = s2.iloc[:,:3]
sag = s2.iloc[:,4:]

veri = pd.concat([sol,sag],axis=1)

# Yeniden oluşturulan 'veri' DataFrame'i, bağımlı değişken olan 'boy' ile birlikte eğitim ve test setlerine bölünür. Özellikler (x_train ve x_test) ile bağımlı değişken (y_train ve y_test) ayrılır.
x_train, x_test,y_train,y_test = train_test_split(veri,boy,test_size=0.33, random_state=0)


# İkinci bir doğrusal regresyon modeli (r2) oluşturulur ve eğitilir. Bu model, özellikler (x_train) ve bağımlı değişken (y_train) üzerinde eğitilir ve test seti (x_test) üzerinde tahminler yapar. Tahmin sonuçları y_pred değişkenine kaydedilir.
r2 = LinearRegression()
r2.fit(x_train,y_train)

y_pred = r2.predict(x_test)


# Bu kod parçası, başlangıçta kategorik verileri sayısal verilere dönüştürme, veri çerçeveleri arasında veri işleme ve iki ayrı doğrusal regresyon modeli oluşturma işlemlerini içerir. İlk model, tahmin yapmak için kullanılan temel bir regresyon modelidir. İkinci model ise bağımlı değişkeni ('boy') tahmin etmek için daha fazla özellik kullanır.
