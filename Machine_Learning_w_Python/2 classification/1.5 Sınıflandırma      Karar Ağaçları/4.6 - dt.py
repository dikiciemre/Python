
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


veriler = pd.read_csv('veriler.csv')
(veriler)

# Bağımsız değişkenler (X) ve bağımlı değişken (y) belirlenir. Bu örnekte, bağımsız değişkenler iloc kullanılarak sütun seçimi ile alınır.
x = veriler.iloc[:,1:4].values #bağımsız değişkenler
y = veriler.iloc[:,4:].values #bağımlı değişken
print(y)



# Veriler, eğitim ve test setleri olarak ayrılır. train_test_split kullanılarak veriler rastgele bir şekilde bölen bir eğitim seti ve test seti olarak ayrılır.
#verilerin egitim ve test icin bolunmesi
from sklearn.model_selection import train_test_split

x_train, x_test,y_train,y_test = train_test_split(x,y,test_size=0.33, random_state=0)


# Veriler, ölçeklendirilir. Bu, bağımsız değişkenlerin farklı ölçeklerde olmasını önlemeye yardımcı olur. Standardizasyon kullanılarak veriler ölçeklenir.
#verilerin olceklenmesi
from sklearn.preprocessing import StandardScaler

sc=StandardScaler()

X_train = sc.fit_transform(x_train)
X_test = sc.transform(x_test)




from sklearn.linear_model import LogisticRegression
logr = LogisticRegression(random_state=0)
logr.fit(X_train,y_train) # İlk olarak, bir lojistik regresyon modeli (LogisticRegression) oluşturulur ve eğitilir (fit fonksiyonu ile).

y_pred = logr.predict(X_test) # Eğitilen model kullanılarak test seti üzerinde tahminler yapılır ve tahmin sonuçları y_pred değişkenine kaydedilir.
print(y_pred)
print(y_test)


from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred) # Confusion matrix (confusion_matrix) kullanılarak modelin performansı değerlendirilir.
print(cm)



from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=1, metric='minkowski') # Model, n_neighbors ve metric gibi parametrelerle yapılandırılır. Bu örnekte, komşu sayısı 1 ve metrik olarak 'minkowski' kullanılmıştır.
knn.fit(X_train,y_train)

y_pred = knn.predict(X_test)

cm = confusion_matrix(y_test,y_pred)
print(cm)


# Bir destek vektör sınıflandırıcı (SVC) modeli oluşturulur ve eğitilir. Radyal tabanlı fonksiyon (RBF) çekirdeği kullanılmıştır.
#Eğitilen model ile tahminler yapılır ve performans confusion matrix ile değerlendirilir.
from sklearn.svm import SVC
svc = SVC(kernel='rbf')
svc.fit(X_train,y_train)

y_pred = svc.predict(X_test)

cm = confusion_matrix(y_test,y_pred)
print('SVC')
print(cm)




#Bir Naive Bayes sınıflandırıcı modeli (GaussianNB) oluşturulur ve eğitilir.
#Eğitilen model ile tahminler yapılır ve performans confusion matrix ile değerlendirilir.
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(X_train, y_train)

y_pred = gnb.predict(X_test)

cm = confusion_matrix(y_test,y_pred)
print('GNB')
print(cm)



# Bir karar ağacı sınıflandırıcı modeli (DecisionTreeClassifier) oluşturulur ve eğitilir. Hata ölçüsü olarak 'entropy' kullanılmıştır.
#Eğitilen model ile tahminler yapılır ve performans confusion matrix ile değerlendirilir.
from sklearn.tree import DecisionTreeClassifier
dtc = DecisionTreeClassifier(criterion = 'entropy')

dtc.fit(X_train,y_train)
y_pred = dtc.predict(X_test)

cm = confusion_matrix(y_test,y_pred)
print('DTC')
print(cm)




# Bu kod, farklı sınıflandırma algoritmalarını kullanarak veri setindeki sınıfları tahmin etmek için bir örnek sunar. Her modelin performansı, confusion matrix ve diğer metrikler kullanılarak değerlendirilir. Bu, veri madenciliği ve sınıflandırma problemleri için başlangıç ​​bir örnek sunar.





