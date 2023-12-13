
#kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#veri yukleme

veriler = pd.read_csv('eksikveriler.csv')

print(veriler)

#eksik veriler

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

Yas = veriler.iloc[:,1:4].values
imputer = imputer.fit(Yas[:,1:4])
Yas[:,1:4] = imputer.transform(Yas[:,1:4])
print(Yas)



# Veri çerçevesinden ülke ve cinsiyet sütunlarını ayırır ve bu verileri ulke ve cinsiyet adlı dizilere saklarsınız.
ulke = veriler.iloc[:,0:1].values

cinsiyet = veriler.iloc[:,-1].values





from sklearn import preprocessing

le = preprocessing.LabelEncoder()
# LabelEncoder kullanarak ülke verilerini sayısal değerlere dönüştürürsünüz.
ulke[:,0] = le.fit_transform(veriler.iloc[:,0])


# Ardından, One-Hot Encoding kullanarak ülke verilerini dönüştürürsünüz. Sonuç, çoklu sütunlu bir dizidir.
ohe = preprocessing.OneHotEncoder()
ulke = ohe.fit_transform(ulke).toarray()
print(ulke)


# Dönüştürülmüş verileri kullanarak üç farklı veri çerçevesi oluşturursunuz.
print(list(range(22)))
sonuc = pd.DataFrame(data=ulke, index = range(22), columns = ['fr','tr','us'])
print(sonuc)

sonuc2 = pd.DataFrame(data=Yas, index = range(22), columns = ['boy','kilo','yas'])
print(sonuc2)

sonuc3 = pd.DataFrame(data = cinsiyet, index = range(22), columns = ['cinsiyet'])
print(sonuc3)

# Bu veri çerçevelerini birleştirerek son veri çerçevesini oluşturursunuz.
s=pd.concat([sonuc,sonuc2], axis=1)
print(s)

s2=pd.concat([s,sonuc3], axis=1)
print(s2)





# Veri setini eğitim ve test setlerine bölersiniz. s veri çerçevesi özelliklerini (x_train ve x_test) ve sonuc3 veri çerçevesini hedef değişken olarak (y_train ve y_test) kullanırsınız. Veri setinin %33'ü test için ayrılmıştır.

from sklearn.model_selection import train_test_split

x_train, x_test,y_train,y_test = train_test_split(s,sonuc3,test_size=0.33, random_state=0)









#(verilerin olceklenmesi) Bu kod, verilerinizi standartlaştırmak için Scikit-Learn kütüphanesinin StandardScaler sınıfını kullanır. Verileri standartlaştırma işlemi, verilerinizi belirli bir ölçekte ve dağılımda olacak şekilde dönüştürmenizi sağlar.
from sklearn.preprocessing import StandardScaler

sc=StandardScaler()

X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)


