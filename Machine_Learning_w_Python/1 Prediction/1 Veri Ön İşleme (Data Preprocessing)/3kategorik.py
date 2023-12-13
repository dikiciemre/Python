
#kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#veri yukleme

veriler = pd.read_csv('eksikveriler.csv')

print(veriler)






#eksik veriler
#sci - kit learn

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy='mean') # fonk tanımlama


Yas = veriler.iloc[:,1:4].values # yas değişkeni tanımlandı
print(Yas)


# İmputer nesnesini fit metoduyla eğitiriz, yani eksik değerleri dolduracak istatistikleri hesaplarız ve bu değerleri transform metoduyla eksik yerlere yerleştiririz. Bu sayede eksik değerler, ortalama değerlerle doldurulmuş olur.
imputer = imputer.fit(Yas[:,1:4]) # eksik olan yerler dolduruldu
Yas[:,1:4] = imputer.transform(Yas[:,1:4])
print(Yas)



ulke = veriler.iloc[:,0:1].values

cinsiyet = veriler.iloc[:,-1].values # cinsiyet tanımlandı








from sklearn import preprocessing

#Bu kod, kategorik (nominal) verileri sayısal verilere dönüştürmek için Label Encoding ve One-Hot Encoding işlemlerini kullanır. 
le = preprocessing.LabelEncoder()

ulke[:,0] = le.fit_transform(veriler.iloc[:,0]) # Bu satırda, LabelEncoder sınıfını içe aktarıyoruz. Label Encoding, kategorik verileri sayısal olarak temsil etmek için kullanılır.
ohe = preprocessing.OneHotEncoder() # Bu satırda, OneHotEncoder sınıfını içe aktarıyoruz. One-Hot Encoding, kategorik verileri sayısal matrislere dönüştürmek için kullanılır.

ulke = ohe.fit_transform(ulke).toarray() #Bu satırda, Label Encoding ile dönüştürdüğümüz 'ulke' dizisini One-Hot Encoding ile dönüştürüyoruz. 
print(ulke)





print(list(range(22)))

sonuc = pd.DataFrame(data=ulke, index = range(22), columns = ['fr','tr','us'])
print(sonuc) # bir veri çerçevesi oluşturuldu




sonuc2 = pd.DataFrame(data=Yas, index = range(22), columns = ['boy','kilo','yas'])
print(sonuc2)






sonuc3 = pd.DataFrame(data = cinsiyet, index = range(22), columns = ['cinsiyet'])
print(sonuc3)




s=pd.concat([sonuc,sonuc2], axis=1)
print(s) # değerleri birleştirir




s2=pd.concat([s,sonuc3], axis=1)
print(s2)

































