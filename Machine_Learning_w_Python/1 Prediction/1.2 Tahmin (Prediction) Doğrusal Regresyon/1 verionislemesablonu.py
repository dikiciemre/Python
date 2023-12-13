


# Bu kod parçası, veri yükleme, eğitim ve test veri setlerine ayırma ve verileri ölçeklendirme işlemlerini içerir.

# Bu kod parçası, veri hazırlama işlemlerini tamamlar ve verileri eğitim ve test veri setleri olarak hazır hale getirir. Bu verileri makine öğrenimi modeline beslemeye hazır hale gelmiştir.

#1.kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

veriler = pd.read_csv('satislar.csv')

print(veriler)


aylar = veriler[['Aylar']]
print(aylar)

satislar = veriler[['Satislar']]
print(satislar)






#verilerin egitim ve test icin bolunmesi
from sklearn.model_selection import train_test_split


# Verilerin yüzde 33'lük bir kısmı test veri seti olarak ayrılırken, geriye kalan yüzde 67'si eğitim veri seti olarak kullanılır. random_state parametresi rastgele bölme işleminin tekrarlanabilirliğini sağlar.
x_train, x_test,y_train,y_test = train_test_split(aylar,satislar,test_size=0.33, random_state=0)





#verilerin olceklenmesi
from sklearn.preprocessing import StandardScaler

sc=StandardScaler()

# Verileri ölçeklendirmek için StandardScaler kullanılır. Eğitim veri seti (x_train) ve test veri seti (x_test) ayrı ayrı ölçeklendirilir. Ölçeklendirme işlemi, verilerin farklı özelliklerinin aynı ölçekte olmasını sağlar ve bazı makine öğrenimi algoritmalarının daha iyi çalışmasına yardımcı olur.
X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)











