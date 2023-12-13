#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 22:02:37 2023

@author: emredikici
"""

import numpy as np
import pandas as pd

# Yapay veri setini oluşturma
np.random.seed(0)
age = np.random.randint(18, 65, 100)  # Yaşları rastgele seçiyoruz
gender = np.random.choice(['Erkek', 'Kadın'], 100)  # Cinsiyetleri rastgele seçiyoruz



# Verileri bir veri çerçevesine (DataFrame) yerleştirme
data = pd.DataFrame({'Yaş': age, 'Cinsiyet': gender})


# Kategorik cinsiyet verisini sayısal forma dönüştürme
data['Cinsiyet'] = data['Cinsiyet'].map({'Erkek': 0, 'Kadın': 1})




from sklearn.model_selection import train_test_split

X = data[['Yaş']]  # Bağımsız değişken (yaş)
y = data['Cinsiyet']  # Bağımlı değişken (cinsiyet)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)




from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, y_train)





y_pred = model.predict(X_test)






from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)
print(f"Model Doğruluğu: {accuracy * 100:.2f}%")





from sklearn.metrics import r2_score

# Gerçek değerler ile tahmin edilen değerler arasındaki R^2 değerini hesapla
r2 = r2_score(y_test, y_pred)

print(f"R^2 Değeri: {r2:.2f}")



