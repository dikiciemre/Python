
#1.kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



# veri yukleme
veriler = pd.read_csv('maaslar.csv')

x = veriler.iloc[:,1:2] # bağımsız x değişkeni
y = veriler.iloc[:,2:] # bağımlı y değişkeni
X = x.values # .values ile pandas DataFrame'lerini NumPy dizilerine dönüştürüyoruz.
Y = y.values





#linear regression ile bir lineer regresyon modeli oluşturuyoruz.
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X,Y) #  ile modeli eğitiyoruz.

plt.scatter(X,Y,color='red') #ile verileri kırmızı renkte nokta grafikleriyle gösteriyoruz.
plt.plot(x,lin_reg.predict(X), color = 'blue') #  ile lineer regresyon tahminlerini mavi renkte bir çizgi grafiğiyle gösteriyoruz.
plt.show()







#polynomial regression
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 2) #ile ikinci dereceden (quadratic) polinom özelliklerini ekleyerek polinom regresyon için bir özellik matrisi oluşturuyoruz.
x_poly = poly_reg.fit_transform(X) #ile bağımsız değişken X'i bu polinom özelliklerine dönüştürüyoruz.
print(x_poly)


lin_reg2 = LinearRegression()
lin_reg2.fit(x_poly,y)
plt.scatter(X,Y,color = 'red')
plt.plot(X,lin_reg2.predict(poly_reg.fit_transform(X)), color = 'blue')
plt.show()








#tahminler

print(lin_reg.predict([[11]])) #ile lineer regresyon modeli kullanarak X=11 için bir tahmin yapıyoruz.
print(lin_reg.predict([[6.6]]))

print(lin_reg2.predict(poly_reg.fit_transform([[6.6]]))) #ile polinom regresyon modeli kullanarak X=6.6 için bir tahmin yapıyoruz.
print(lin_reg2.predict(poly_reg.fit_transform([[11]])))






#verilerin olceklenmesi
from sklearn.preprocessing import StandardScaler

sc1=StandardScaler()

x_olcekli = sc1.fit_transform(X) #Bağımsız değişken X'i sc1 ile ölçeklendiriyoruz ve x_olcekli adında yeni bir değişkene atıyoruz.

sc2=StandardScaler()
y_olcekli = np.ravel(sc2.fit_transform(Y.reshape(-1,1))) # Bağımlı değişken Y'yi de sc2 ile ölçeklendiriyoruz ve y_olcekli adında yeni bir değişkene atıyoruz.





from sklearn.svm import SVR

svr_reg = SVR(kernel='rbf') # SVR modelini oluşturmak için SVR(kernel='rbf') kullanılır. RBF (Radial Basis Function) çekirdeği kullanılmıştır.
svr_reg.fit(x_olcekli,y_olcekli) # ile SVR modelini ölçeklenmiş verilere uyarlarız.

plt.scatter(x_olcekli,y_olcekli,color='red') # Ölçeklenmiş verileri kırmızı renkte nokta grafikleriyle gösterir ve SVR'nin tahminlerini mavi bir çizgi grafiğiyle gösteririz.
plt.plot(x_olcekli,svr_reg.predict(x_olcekli),color='blue')


print(svr_reg.predict([[11]])) #Son olarak, SVR ile X=11 ve X=6.6 için tahminler yaparız ve sonuçları görüntüleriz.
print(svr_reg.predict([[6.6]]))













