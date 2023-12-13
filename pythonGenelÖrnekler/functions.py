





#kullanıcıdan input alarak hesap makinesi
"""
def topla(sayi1, sayi2):
    result = sayi1 + sayi2
    print("sonuc değeri: ", result)


def cikar(sayi1, sayi2):
    result = sayi1 - sayi2
    print("sonuc değeri: ", result)


def carp(sayi1, sayi2):
    result = sayi1 * sayi2
    print("sonuc değeri: ", result)


def bol(sayi1, sayi2):
    result = sayi1 // sayi2
    print("sonuc değeri: ", result)


print("YAPMAK İSTEDİĞİNİZ İŞLEMİ SEÇİNİZ\n 1-)+\n 2-)-\n 3-)*\n 4-)%")
islem = input("islem seçiniz..")

print("işlem yapmak istediğiniz sayıları giriniz..\n")
sayi1 = input("sayi1: ")
sayi2 = input("sayi2: ")

if (islem == 1):
    topla(sayi1, sayi2)
elif (islem == 2):
    cikar(sayi1, sayi2)
elif (islem == 3):
    carp(sayi1, sayi2)
elif (islem == 4):
    bol(sayi1, sayi2)
else:
    print("\nSENİN NE İŞİN VAR BURDA!!!!!!")
"""






#kafama göre yazdım

"""
def lovePrint(name,surname):
    print("seni çok seviyorum "+ name + surname)

name = input("isim değeri: ")
surname = input("soy isim değeri: ")

lovePrint(name,surname)
"""












#Gönderilen 2 sayı arasındaki tüm asal sayıları bulan ve toplayan python fonksiyon uygulamasını yapınız.
"""
toplam =0
sayi1 = int(input('sayı 1:'))
sayi2 = int(input('sayı 2:'))

for i in range(sayi1,sayi2):
    toplam += i

def asalSayılariBul(sayi1, sayi2):
    for sayi in range(sayi1, sayi2+1):
        if sayi > 1:
            for i in range(2, sayi):
                if (sayi % i == 0):
                    break
            else:
                print(sayi)
print("toplamları: {}".format(toplam))
asalSayılariBul(sayi1, sayi2)
"""












#dictionary yapısı ile istenilen değeri kullanıcıdan alarak bastırma

"""
print("Kütüphane'nin İnternet Sitesi'ne Hoş Geldiniz")

kitaplar = {"Vatan Yahut Silistre": "Namık Kemal",
"Ütopya": "Thomas More",
"Eylül": "Mehmet Rauf",
"İlyada": "Homeros",
"Kürk Mantolu Madonna": "Sabahattin Ali",
"Yabancı": "Albert Camus",
"Aşk": "Elif Şafak",
"Otostopçunun Galaksi Rehberi": "Douglas Adams"}



eserler = [i for i in kitaplar.keys()]
yazarlar = [i for i in kitaplar.values()]

while True:
    secim = int(input(
        " -------------\n Eserleri görmek için 1 \n Yazarları görmek için 2 \n Eserleri ve Yazarları görmek için 3 \n Çıkmak için başka bir şey yazınız:\n ------------- "))

    if secim == 1:
        for i in eserler:
            print("-" + i)

    elif secim == 2:
        for i in yazarlar:
            print("-" + i)

    elif secim == 3:
        for i in kitaplar.items():
            print(i)

    else:
        break

"""










#EBOB BULMA

"""
def ebob(a, b):

    ebob = None

    if a > b:
        fark = a - b

    elif a < b:
        fark = b - a

    else:
        fark = 0  # a == b

    # Aradaki farkın mutlak değerini aldık.

    if fark == 0:

        ebob = a
    # Eğer fark sıfırsa ebob sayılardan herhangi birine eşit olur.

    else:
        for i in range(1, fark + 1):  # Sıfırdan farka kadar olan sayılarda gezindik.
            if a % i == 0 and b % i == 0:  # Eğer i, a ve b yi tam bölüyorsa if bloğuna girdi.
                ebob = i  # ebob'un değeri a ve b yi kalansız bölebilen en son i değeri oldu. Yani bölenlerin en büyüğü.

    print(ebob)



a = int(input("ebob alınacak ilk sayıyı giriniz.."))
b = int(input("ebob alınacak ilk sayıyı giriniz.."))

ebob(a,b)

"""










#EKOK BULMA

"""

def ekok(a, b):

    ekok = None

    if a > b:
        fark = a - b

    elif a < b:
        fark = b - a

    else:
        fark = 0  # a == b

    # ebob örneğindeki gibi farkın mutlak değerini aldık

    if fark == 0:

        ekok = a
    # Eğer fark sıfırsa ekok sayılardan herhangi birine eşit olur.

    else:
        ekok = (a * b) / fark

    return ekok



a = float(input("ekok alınacak ilk sayıyı giriniz.."))
b = float(input("ekok alınacak ilk sayıyı giriniz.."))

ekok(a,b)
"""










#DAİRENİN ALANINI VE YA ÇEVRESİNİ DEĞERLERİ KULLANICIDAN GİREREK HESAPLAYAN PROGRAM

"""
print("DAİREDE ALAN VE YA ÇEVRE HESAPLAMA PROGRAMINA HOŞ GELDİNİZ..\n")
PI = 3.14

r = int(input("hesaplamak istediğiniz dairenin yarıçap değerini giriniz : "))

print("hangi değeri hesaplamak istersiniz :\n")
select = int(input("1-) ALAN 2-) ÇEVRE : "))

if(select == 1):
    print("Dairenin Alanı : {} dır".format(PI*r*r))
elif(select == 2):
    print("Dairenin çevresi : {} dır".format(2*PI*r))
else:
    print("WARNİNG!!!")
"""











#ÜSSÜNÜ ALAN FONKSİYON

"""
def usal(a,b):#a taban değeri b üs değeri yani a yı b kere çarpıcaz
    sonuc = a**b
    print("{} değerinin {}. kuvveti {} değerine eşittir.".format(a,b,sonuc))


a = int(input("taban değerini giriniz.."))
b = int(input("üs değerini giriniz.."))

usal(a,b)

"""






















