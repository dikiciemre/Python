

#1.kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import r2_score

# veri yukleme
veriler = pd.read_csv('maaslar.csv')

x = veriler.iloc[:,2:4] #  ile bağımsız değişkenleri X'e atıyoruz.
y = veriler.iloc[:,4:] # ile bağımlı değişkenleri Y'ye atıyoruz.

X = x.values # .values ile pandas DataFrame'lerini NumPy dizilerine dönüştürüyoruz.
Y = y.values



# İlk olarak, Doğrusal Regresyon modeli oluşturulur, eğitilir ve tahminler yapılır. Ayrıca, bu modelin tahminlerini görselleştiren bir grafik çizilir ve R-kare değeri hesaplanır.
#linear regression
from sklearn.linear_model import LinearRegression

lin_reg = LinearRegression()
lin_reg.fit(X,Y) # lin_reg.fit(X, Y) ile modeli bağımsız değişken X ve bağımlı değişken Y ile eğitiyoruz.

plt.scatter(X,Y,color='red') # Tahminleri görselleştirmek için bir grafik oluşturuyoruz.
plt.plot(x,lin_reg.predict(X), color = 'blue')
plt.show()

print('Linear R2 degeri')
print(r2_score(Y, lin_reg.predict(X)))



# Ardından, Polinom Regresyon modeli oluşturulur ve eğitilir. Tahminler yapılır, tahminleri görselleştiren bir grafik çizilir ve R-kare değeri hesaplanır.
#polynomial regression
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 2)
x_poly = poly_reg.fit_transform(X)
print(x_poly)
lin_reg2 = LinearRegression()
lin_reg2.fit(x_poly,y)
plt.scatter(X,Y,color = 'red')
plt.plot(X,lin_reg2.predict(poly_reg.fit_transform(X)), color = 'blue')
plt.show()




#tahminler

print(lin_reg.predict([[11]]))
print(lin_reg.predict([[6.6]]))

print(lin_reg2.predict(poly_reg.fit_transform([[6.6]])))
print(lin_reg2.predict(poly_reg.fit_transform([[11]])))

print('Polynomial R2 degeri') # R-kare (R-squared) değeri, tahmin performansını değerlendirmek için kullanılır ve yazdırılır.
print(r2_score(Y, lin_reg2.predict(poly_reg.fit_transform(X))))



# Verilerin ölçeklenmesi için StandardScaler kullanılır ve bu ölçeklenmiş verilerle Destek Vektör Regresyonu (SVR) modeli oluşturulur. SVR modeli eğitilir, tahminler yapılır, tahminleri görselleştiren bir grafik çizilir ve R-kare değeri hesaplanır.
#verilerin olceklenmesi
from sklearn.preprocessing import StandardScaler

sc1=StandardScaler()
# Bağımsız değişken X ve bağımlı değişken Y, StandardScaler kullanılarak ölçeklenir.
x_olcekli = sc1.fit_transform(X)

sc2=StandardScaler()
y_olcekli = np.ravel(sc2.fit_transform(Y.reshape(-1,1)))



#Destek Vektör Regresyonu (SVR) modeli oluşturulur, eğitilir ve tahminler yapılır.
from sklearn.svm import SVR

svr_reg = SVR(kernel='rbf')
svr_reg.fit(x_olcekli,y_olcekli)

plt.scatter(x_olcekli,y_olcekli,color='red')
plt.plot(x_olcekli,svr_reg.predict(x_olcekli),color='blue')

plt.show()
print(svr_reg.predict([[11]]))
print(svr_reg.predict([[6.6]]))

print('SVR R2 degeri')
print(r2_score(y_olcekli, svr_reg.predict(x_olcekli)))



# Karar Ağacı Regresyon modeli (Decision Tree Regressor) oluşturulur, eğitilir ve tahminler yapılır. Tahminler görselleştirilir ve R-kare değeri hesaplanır.
#Decision Tree Regresyon
from sklearn.tree import DecisionTreeRegressor
r_dt = DecisionTreeRegressor(random_state=0)
r_dt.fit(X,Y)
Z = X + 0.5
K = X - 0.4

plt.scatter(X,Y, color='red')
plt.plot(x,r_dt.predict(X), color='blue')
plt.plot(x,r_dt.predict(Z),color='green')
plt.plot(x,r_dt.predict(K),color='yellow')
plt.show()
print(r_dt.predict([[11]]))
print(r_dt.predict([[6.6]]))

print('Decision Tree R2 degeri')
print(r2_score(Y, r_dt.predict(X)))




# Random Forest Regresyon modeli oluşturulur, eğitilir ve tahminler yapılır. Tahminler görselleştirilir ve R-kare değeri hesaplanır.
#Random Forest Regresyonu
from sklearn.ensemble import RandomForestRegressor
rf_reg=RandomForestRegressor(n_estimators = 10,random_state=0) # RandomForestRegressor ile bir rastgele orman regresyon modeli oluşturulur. n_estimators parametresi, kullanılan karar ağaçlarının sayısını belirtir.
rf_reg.fit(X,Y.ravel())

print(rf_reg.predict([[6.6]]))

# Model eğitilir ve tahminler yapılır.
plt.scatter(X,Y,color='red')
plt.plot(X,rf_reg.predict(X),color='blue')

plt.plot(X,rf_reg.predict(Z),color='green')
plt.plot(x,r_dt.predict(K),color='yellow')
plt.show()






# Tahmin sonuçları ve R-kare değerleri yazdırılır.
print('Random Forest R2 degeri')
print(r2_score(Y, rf_reg.predict(X)))

print(r2_score(Y, rf_reg.predict(K)))
print(r2_score(Y, rf_reg.predict(Z)))

#Ozet R2 değerleri
print('-----------------------')
print('Linear R2 degeri')
print(r2_score(Y, lin_reg.predict(X)))

print('Polynomial R2 degeri')
print(r2_score(Y, lin_reg2.predict(poly_reg.fit_transform(X))))

print('SVR R2 degeri')
print(r2_score(y_olcekli, svr_reg.predict(x_olcekli)))


print('Decision Tree R2 degeri')
print(r2_score(Y, r_dt.predict(X)))

print('Random Forest R2 degeri')
print(r2_score(Y, rf_reg.predict(X)))



