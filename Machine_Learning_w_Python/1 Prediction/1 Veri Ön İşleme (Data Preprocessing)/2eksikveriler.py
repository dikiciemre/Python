
#kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#kodlar
#veri yukleme

veriler = pd.read_csv('eksikveriler.csv')
#pd.read_csv("veriler.csv")

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



































