

"""


#tek sayıları bastırma
for i in range(1,10,2):
    print(i)

print("----------------------")


#çift sayıları bastırma
for i in range(0,10,2):
    print(i)

print("----------------------")

for i in range(10):
    print("Emre DİKİCİ")
"""






"""

araba_modelleri=["BMW","mercedes","alfa romeo","wolsvagen","mini cooper","audi"]
araba_yili = 2018
for araba in araba_modelleri:

    araba_yili = araba_yili + 1
    print(araba_yili,araba)
    
"""









#DEĞERLER ARASINDAKİ DAYILARIN TOPLAMI
"""
toplam = 0;
sayi1 = input('1. Sayı: ')
sayi2 = input('2. Sayı: ')
for i in range(int(sayi1) + 1, int(sayi2)):
    toplam += i
    print("{0} ile {1} arasındaki sayıların toplamı : {2}".format(sayi1, sayi2, toplam))
"""









#FAKTÖRİYEL ALMA

"""
sonuc=1;
sayi=input('1. Sayı: ')
for i in range(1,int(sayi)+1):
      sonuc*=i
print("{0} sayısının faktoriyeli : {1}".format(sayi,sonuc))
"""











#ÇARPIM TABLOSU

"""
for i in range(1, 11):
    for j in range(1, 11):
        print("{} x {} = {}".format(i, j, i * j))
    print("\n")

"""
