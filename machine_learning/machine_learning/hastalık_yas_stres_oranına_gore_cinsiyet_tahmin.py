#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 22:14:03 2023

@author: emredikici
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Örnek veri setini oluşturma
np.random.seed(0)
n_samples = 100

# Rastgele yaş değerleri oluşturma (18 ile 65 arasında)
yas = np.random.randint(18, 66, n_samples)

# Rastgele cinsiyet değerleri oluşturma (Erkek ve Kadın)
cinsiyet = np.random.choice(['Erkek', 'Kadın'], n_samples)

# Rastgele kronik hastalık durumu oluşturma (0: Yok, 1: Var)
kronik_hastalik = np.random.randint(2, size=n_samples)

# Rastgele stres oranı oluşturma (0 ile 10 arasında)
stres_orani = np.random.randint(0, 11, n_samples)

# Veri çerçevesi oluşturma
veri = pd.DataFrame({'Yaş': yas, 'Cinsiyet': cinsiyet, 'Kronik Hastalık': kronik_hastalik, 'Stres Oranı': stres_orani})

# Veri setini eğitim ve test kümelerine bölelim
X = veri[['Yaş', 'Kronik Hastalık', 'Stres Oranı']]
y = veri['Cinsiyet']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modeli eğitme (Random Forest sınıflandırıcı kullanıyoruz)
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)



# Modeli kullanarak tahminlerde bulunma
yas_input = 30  # Örnek yaş girdisi
hastalik_input = 1  # Örnek hastalık girdisi (0: Yok, 1: Var)
stres = 3

# Tahmin işlemi için verileri bir DataFrame'e yerleştirme
tahmin_verisi = pd.DataFrame({'Yaş': [yas_input], 'Kronik Hastalık': [hastalik_input],'Stres Oranı': [stres]})

# Modeli kullanarak cinsiyet tahmini yapma
tahmin = model.predict(tahmin_verisi)

print(f"Yaş: {yas_input}, Kronik Hastalık: {'Var' if hastalik_input == 1 else 'Yok'},Stres Oranı : {stres}  Tahmin Edilen Cinsiyet: {tahmin[0]}")


# Modelin başarı değerini hesaplama
basari = model.score(X_test, y_test)
print(f"Model Başarı Değeri: {basari * 100:.2f}%")
