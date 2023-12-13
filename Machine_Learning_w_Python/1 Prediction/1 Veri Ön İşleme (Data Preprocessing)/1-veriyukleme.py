
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd




veri = pd.read_csv('veriler.csv') # veriler.csv den datalar çekildi
boy = veri[['boy']] # boy değeri alındı
print(boy)


boykilo = veri[['boy','kilo']] #boy ve kilo değerleri ayrı olarak çağırıldı
print(boykilo)


kiloyas = veri[['kilo','yas']] #yas ve kilo değerleri ayrı olarak çağırıldı
print(kiloyas)