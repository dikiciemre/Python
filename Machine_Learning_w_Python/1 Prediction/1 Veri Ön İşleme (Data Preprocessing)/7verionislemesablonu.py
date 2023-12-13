
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


veriler = pd.read_csv('veriler.csv')

print(veriler)

x = veriler.iloc[:,1:4].values #bağımsız değişkenler
y = veriler.iloc[:,4:].values #bağımlı değişken





#verilerin egitim ve test icin bolunmesi
from sklearn.model_selection import train_test_split

x_train, x_test,y_train,y_test = train_test_split(x,y,test_size=0.33, random_state=0)





#verilerin olceklenmesi
from sklearn.preprocessing import StandardScaler

sc=StandardScaler()

X_train = sc.fit_transform(x_train)
X_test = sc.transform(x_test)





from sklearn.linear_model import LogisticRegression # Bu satırda, lojistik regresyon modelini içe aktarıyoruz. 

logr = LogisticRegression(random_state=0) # Bu satırda, bir LogisticRegression nesnesi oluşturuyoruz. random_state=0 parametresi, modelin rastgele başlatma işlemlerini tekrarlanabilir hale getirir.
logr.fit(X_train,y_train) # Bu satırda, lojistik regresyon modelini eğitiyoruz. X_train, eğitim veri kümesini ve y_train, eğitim veri kümesine karşılık gelen hedef etiketlerini temsil eder. 

y_pred = logr.predict(X_test) # Bu satırda, eğitilmiş lojistik regresyon modelini kullanarak test veri kümesi (X_test) üzerinde tahminler yaparız. 
print(y_pred)
print(y_test)

















