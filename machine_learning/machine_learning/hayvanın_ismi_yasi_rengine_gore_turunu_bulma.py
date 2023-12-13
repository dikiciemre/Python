#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 23:12:26 2023

@author: emredikici
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import r2_score



# Veri setini oluşturma
veri = {
    'Hayvan İsmi': ['Köpek', 'Kedi', 'Kuş', 'At', 'Kaplumbağa', 'Tavşan', 'Köpekbalığı', 'Kedi', 'Tavşan'],
    'Tür': ['Memeli', 'Memeli', 'Kuş', 'Memeli', 'Sürüngen', 'Memeli', 'Balık', 'Memeli', 'Memeli'],
    'Yaş': [5, 3, 2, 7, 1, 4, 10, 2, 3],
    'Renk': ['Siyah', 'Beyaz', 'Kahverengi', 'Kahverengi', 'Yeşil', 'Kahverengi', 'Gri', 'Siyah', 'Kahverengi']
}

# Pandas DataFrame oluşturma
hayvanlar_df = pd.DataFrame(veri)

# Veriyi sayısal formata dönüştürme
label_encoder_hayvan_ismi = LabelEncoder()
label_encoder_renk = LabelEncoder()
label_encoder_tur = LabelEncoder()

hayvanlar_df['Hayvan İsmi'] = label_encoder_hayvan_ismi.fit_transform(hayvanlar_df['Hayvan İsmi'])
hayvanlar_df['Renk'] = label_encoder_renk.fit_transform(hayvanlar_df['Renk'])
hayvanlar_df['Tür'] = label_encoder_tur.fit_transform(hayvanlar_df['Tür'])


# Veri setini eğitim ve test kümelerine bölelim
X = hayvanlar_df[['Hayvan İsmi', 'Yaş', 'Renk']]
y = hayvanlar_df['Tür']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modeli eğitme
model = LogisticRegression()
model.fit(X_train, y_train)

# Modeli kullanarak tahminlerde bulunma
Hayvan_ismi_input = 'Kedi'
yas_input = 7
renk_input = 'Yeşil'

# Tahmin işlemi için verileri bir DataFrame'e yerleştirme
tahmin_verisi = pd.DataFrame({'Hayvan İsmi': [label_encoder_hayvan_ismi.transform([Hayvan_ismi_input])[0]], 'Yaş': [yas_input], 'Renk': [label_encoder_renk.transform([renk_input])[0]]})

# Modeli kullanarak tür tahmini yapma
tahmin = model.predict(tahmin_verisi)

# Tahmini türü etikete geri çevirme
tahmin_tur = label_encoder_tur.inverse_transform(tahmin)

# Sonucu gösterme
print(f"Yaş: {yas_input}, Hayvan İsmi: {Hayvan_ismi_input}, Renk: {renk_input}, Tahmin Edilen Tür: {tahmin_tur[0]}")
















