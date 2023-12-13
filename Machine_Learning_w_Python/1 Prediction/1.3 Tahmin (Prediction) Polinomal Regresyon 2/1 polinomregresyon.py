
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










