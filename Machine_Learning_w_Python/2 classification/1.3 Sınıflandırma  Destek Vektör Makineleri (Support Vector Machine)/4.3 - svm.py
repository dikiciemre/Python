
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






from sklearn.svm import SVC
svc = SVC(kernel='poly') # SVC(kernel='poly') ile bir Destek Vektör Makinesi (SVM) modeli oluşturuyoruz. kernel parametresi, kullanılacak çekirdek fonksiyonunu belirtir ve bu durumda "poly" (polinom) çekirdeği kullanılır. Polinom çekirdeği, veriyi yüksek boyutlu uzaya dönüştürerek daha karmaşık sınıflandırma problemlerini çözmeye yardımcı olur.
svc.fit(X_train,y_train) # Oluşturulan SVM modelini eğitmek için fit yöntemini kullanırız. Model, eğitim verileri (X_train ve y_train) ile eğitilir.

y_pred = svc.predict(X_test) # Eğitilmiş SVM modelini kullanarak predict yöntemini kullanarak test verileri (X_test) üzerinde tahminler yaparız ve tahmin sonuçlarını y_pred değişkenine kaydederiz.

cm = confusion_matrix(y_test,y_pred) # Confusion matrix, bir sınıflandırma modelinin performansını değerlendirmek için kullanılır. confusion_matrix fonksiyonu kullanılarak gerçek test verileri (y_test) ile modelin tahmin ettiği veriler (y_pred) arasındaki karşılaştırmayı yaparız ve sonucu cm değişkenine kaydederiz.
print('SVC')
print(cm)









