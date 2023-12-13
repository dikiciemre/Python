
#1.kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#2.veri onisleme
#2.1.veri yukleme
veriler = pd.read_csv('veriler.csv')
#pd.read_csv("veriler.csv")
#test
print(veriler)

x = veriler.iloc[:,1:4].values #bağımsız değişkenler
y = veriler.iloc[:,4:].values #bağımlı değişken
print(y)


#verilerin egitim ve test icin bolunmesi
from sklearn.model_selection import train_test_split

x_train, x_test,y_train,y_test = train_test_split(x,y,test_size=0.33, random_state=0)



#verilerin olceklenmesi
from sklearn.preprocessing import StandardScaler

sc=StandardScaler()

X_train = sc.fit_transform(x_train)
X_test = sc.transform(x_test)





from sklearn.linear_model import LogisticRegression
logr = LogisticRegression(random_state=0)
logr.fit(X_train,y_train)

y_pred = logr.predict(X_test) # predict yöntemi ile model, test verileri (X_test) üzerinde tahminler yapar ve sonuçları y_pred değişkenine kaydederiz.
print(y_pred)
print(y_test)






from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)
print(cm)



from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=1, metric='minkowski') # KNeighborsClassifier ile bir KNN modeli oluşturulur. n_neighbors parametresi, kullanılacak komşu sayısını belirtir.
knn.fit(X_train,y_train) # Model, eğitim verileri (X_train ve y_train) ile eğitilir.


y_pred = knn.predict(X_test) # KNN modeli, aynı şekilde predict yöntemi ile test verileri üzerinde tahminler yapar ve sonuçları y_pred değişkenine kaydederiz.

cm = confusion_matrix(y_test,y_pred) # KNN modelinin performansı da aynı şekilde confusion_matrix kullanılarak değerlendirilir.
print(cm)













