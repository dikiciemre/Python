#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 22:08:26 2023

@author: emredikici
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Örnek veri setini oluşturma
np.random.seed(0)
n_samples = 1000

# Rastgele yaş değerleri oluşturma (18 ile 65 arasında)
yas = np.random.randint(18, 66, n_samples)

# Rastgele cinsiyet değerleri oluşturma (Erkek ve Kadın)
cinsiyet = np.random.choice(['Erkek', 'Kadın'], n_samples)

# Rastgele hastalık değerleri oluşturma (0: Yok, 1: Var)
hastalik = np.random.randint(2, size=n_samples)

# Veri çerçevesi oluşturma
veri = pd.DataFrame({'Yaş': yas, 'Cinsiyet': cinsiyet, 'Hastalık': hastalik})

# Veri setini eğitim ve test kümelerine bölelim
X = veri[['Yaş', 'Hastalık']]
y = veri['Cinsiyet']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modeli eğitme
model = LogisticRegression()
model.fit(X_train, y_train)

# Modeli kullanarak tahminlerde bulunma
yas_input = 30  # Örnek yaş girdisi
hastalik_input = 1  # Örnek hastalık girdisi (0: Yok, 1: Var)

# Tahmin işlemi için verileri bir DataFrame'e yerleştirme
tahmin_verisi = pd.DataFrame({'Yaş': [yas_input], 'Hastalık': [hastalik_input]})

# Modeli kullanarak cinsiyet tahmini yapma
tahmin = model.predict(tahmin_verisi)

# Sonucu gösterme
print(f"Yaş: {yas_input}, Hastalık: {'Var' if hastalik_input == 1 else 'Yok'}, Tahmin Edilen Cinsiyet: {tahmin[0]}")
