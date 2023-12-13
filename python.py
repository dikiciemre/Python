# This is a sample Python script.



"""
hava="puslu"

if hava=="puslu":
    print("dışarı çıkma")
 elif hava=="pussuz":
    print("çık çık")

  else:
   print("bu nası iş")
"""
import datetime
import re

"""
liste=["a","b","c"]
hedef="a"
if hedef in liste:
    print("bulduk bulduk")
else:
   print("bulamadık")
"""





"""
liste=["b","a","c"]
hedef="a"

if (hedef=="a") and (hedef in liste[0] ):
    print("harf var ve ilk sırada")

elif (hedef=="a"):
    print(" sadece harf var")

else:
    print("bozuk bu aq")
"""





"""
sayilar=[1,3,5,7,9,11]

for sayi in sayilar:  #sayilar kümesini sırayla yazar
    print(sayi)
"""



"""
sinif_listesi=["emre dikici","oğuz agam","selim garip","enişte diyafram"]

for kullanici in sinif_listesi:
    print(kullanici)
print("\n")


sinif_listesi=["emre dikici","oğuz agam","selim garip","enişte diyafram"]
kullanici_sayisi=0
for kullanici in sinif_listesi:
    kullanici_sayisi=kullanici_sayisi+1
    print(kullanici,kullanici_sayisi)
"""





"""

araba_modelleri=["BMW","mercedes","alfa romeo","wolsvagen","mini cooper","audi"]
araba_yili = 2018
for araba in araba_modelleri:

    araba_yili = araba_yili + 1
    print(araba_yili,araba)
"""




"""
liste=[[1,3],[5,6]]

for sayi1,sayi2 in liste:
    print(sayi1) # 1 ve 5 değerlerini bastırır
"""





"""
liste=[[1,3],[5,6]]
for sayi1,sayi2 in liste:
    print(sayi2)#3 ve 6 değerlerini bastırır
"""






"""
x = 0
while x < 16:
    print("{} değeri 16 dan küçüktür".format(x))
    x = x+1
else:
    print("{} değeri 16 dan küçük değildir".format(x))
"""





"""
sayi=6
sonuc=1

while sayi>0:
    sonuc=sonuc*sayi     #faktoriyel hessaplama
    sayi=sayi-1
    print(sonuc)

"""






"""
print(range(10)) #0 dan 10 a kadar olan değerleri içerir 10 yok

print(list(range(10))) #0 dan 10 a kadar olan değerleri listeler

print(list(range(3,10))) # 3 dahill 10 a kadar olan sayıları yazar

print(list(range(3,10,2)))

"""






"""
for sayi in range(20):
    if sayi > 10:         #10 ile 20 arasındaki sayılları yazdırır
        print(sayi)
  """







"""
harfler=["a","b","c","d","e","f","g"]

for harf in enumerate(harfler):
    print(harf)          #harflere sıra numarası verir
"""






"""

harfler=["a","b","c","d","e","f","g"]

for index ,harf in enumerate(harfler):
    print(index , harf)          #harflere sıra numarası verir
"""






"""
harfler=["a","b","c","d","e","f","g"]

for index ,harf in enumerate(harfler):
    print("{} . harf = {}".format(index,harf))

"""




"""
kullanici1 = {

    "isim" : "emre",
    "soyad" : "dikici",
    "work" : "software",
}

kullanici2 = {

    "isim": "selim",
    "soyad": "garip",
    "work": "developer",
}

kul_liste = [kullanici1 , kullanici2]

for kullanici in kul_liste:
    if kullanici.get("work") == "developer":
        print(kullanici.get("isim"))
"""






"""
pet1 = {

    "name" : "patrick",
    "surname" : "wilson",
    "type" : "golden",
}

pet2 = {

    "name": "john",
    "surname": "wilson",
    "type": "karabas",
}

pet3 = {

    "name": "david",
    "surname": "backham",
    "type": "golden",
}


pet_list = [pet1,pet2,pet3]
number=0
for pet in pet_list:
    if pet.get("name") == "patrick":
        number=number+1
        print("{}. pet name is {}".format(number,pet.get("name")))

for pet in pet_list:
    if pet.get("surname") == "wilson":
        number = number + 1
        print("{} .pet surname is {}".format(number,pet.get("surname")))
"""




#FOR DÖNGÜSÜ ÖRNEKLERİ:
"""
for x in range(5):
    print(x)
 """


"""
#ÇİFT SAYI YAZDIRMA
for sayi in range(20):
    if sayi % 2 ==0:
        print(sayi)
"""

#ÇİFT SAYI YAZDIRMA

"""
for sayi in range(20):
    if sayi % 2 !=0:
        print(sayi)
"""


#BİR YAZIYI 10 KEERE YAZDIRMA
"""
for x in range(10):
    print(" efe aydoğmuş")
"""


#KULLANICIDAN İSTEYEREK YAZDIRMA
"""
metin = input()
for x in range(10):
    print(metin)
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






"""
print(list(range(3,6)))
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








#FUNCTİONS
"""
def uc_bastir():
    print(3)       #uc bastır adında bir fonksiyon oluşpturuldu ve o fonksiyona print(3) diyerek 3 basması söylendi
                 
uc_bastir()

"""





"""
def uc_bastir():
    print(3)  
    
a = uc_bastir()

print(a)

"""





"""
def sayi_dondur(sayi):
    print(sayi) 

sayi_dondur(456)

"""




"""
def karesini_al(x):
    return x**2

sayilar=list(range(1,6))
print(sayilar)

#for index in range(len(sayilar)):
for index in range(5):
    sayilar[index] = karesini_al(sayilar[index])
print(sayilar)


"""





"""
def cift_sayi(x):
    if x % 2 == 0:
        return x

print(cift_sayi(4))

"""




"""
# RANGE VERDİĞİMİZ SAYILAR ARSINDA ÇİFT SAYILARI BULMA

sayilar = range(50)
def cift_sayi(x):
    if x % 2 == 0:
        return x

print(list(filter(cift_sayi,sayilar)))

"""




# RANGE VERDİĞİMİZ SAYILAR ARASINDA TEK SAYILARI BULMA
"""
sayilar = range(100)

def tek_sayi_bulma(x):
    if x % 2 != 0:
        return x

print(list(filter(tek_sayi_bulma,sayilar)))

"""





#KOLAY YOLDAN KARESİ ALMA
"""
sayilar = [1,2,3,4,5,6]

print(list(map(lambda sayi: sayi**2,sayilar)))
"""



#İKİ SAYI TOPLAMI VE FARKI VEREN FONKSİYON
"""
def toplam(a,b):
    return a+b

def cikarma(a,b):
    return a-b

print(toplam(8,3))
print(cikarma(8,4))
"""





#yaş hesaplama fobksiyınu

"""
def yas_hesapla(x):
    return 2022-x

age_emre = yas_hesapla(2003)
print(age_emre)

age_selim = yas_hesapla(2006)
print("selim {} yaşındadır ".format(age_selim))

"""



#input alma
"""
sayi=input("sayi girisi yapiniz")
print("Sayi {} degerine esittir".format(sayi) )
"""




#SAYI TİPİ DEĞİŞKEN KONTROL ETME
"""
girdi = input("sayi girisi yapiniz")

if girdi.isdigit():     #İSDİGİT KOMUTU KODUN SAYİ TİPİ OLUP OLMADIĞINI SORGULAR
    print("{} sayı tipidir".format(girdi))
else:
    print(" {} yanlış bir girdi!!!!".format(girdi))
"""





#DAİRE ALAN BULMA
"""
def daire_alan(yaricap):
    alan = int(yaricap) * int(yaricap) * 3,14
    print("alan = {}".format(alan))

yaricap = input("yaricap bilgisi giriniz...")
print("dairenin yaricapı {} ".format(yaricap))
daire_alan(yaricap)
"""





#ÜÇGEN ALAN BULMA

"""
def ucgen_alan(alt,ust):
    alan = (float(alt) * float(ust))/2
    print("alan = {}".format(alan))

alt = input("alt taban uzunluğu giriniz : ")
ust = input("ust taban uzunluğu giriniz : ")

ucgen_alan(alt,ust)

"""






# DİKDÖRTGEN ALAN BULMA

"""
def dik_alan(ust,alt):
    alan = float(ust) * float(alt)
    print("dikdortgen {} alanına sahiptir.".format(alan))

alt = input("alt girisi yapınız..")
ust = input("ust girisi yapınız..")
dik_alan(alt,ust)
"""






#girilen degeri yuvarlama
"""

def tam_sayi():
    girdi = input("tam sayiya cevirilecek degeri yaziniz.")

    try:
        girdi = float(girdi)
        print("yuvarlama sonucu : {}".format(round(girdi)))

    except:
        print("{} girdisi ondaliga cevrilemiyor.".format(girdi))
        
tam_sayi()

"""






"""
def tam_sayi():
    girdi = input("tam sayiya cevirilecek degeri yaziniz.")

    try:
        girdi = float(girdi)

    except:
        print("{} girdisi ondaliga cevrilemiyor.".format(girdi))

    else:
        print("yuvarlama sonucu : {}".format(round(girdi)))
tam_sayi()

"""






"""
def tam_sayi():
    girdi = input("tam sayiya cevirilecek degeri yaziniz.")
    status = ""
    try:
        girdi = float(girdi)
        print("yuvarlama sonucu : {}".format(round(girdi)))
        status = "basarili"
    except:
        print("{} girdisi ondaliga cevrilemiyor.".format(girdi))
        status = "basarisiz"
    finally:
        print("statu {} olarak degerlendirildi.".format(status))

tam_sayi()

"""






"""
def tam_sayi():

    while True:

        girdi = input("tam sayiya cevirilecek degeri yaziniz")

        try:
            girdi = float(girdi)
            print("yuvarlama sonucu {} ".format(round(girdi)))
            break

        except:
            print("{} girdisi ondaliga cevrilemiyor.".format(girdi))
            pass

tam_sayi()

"""






#SAYININ KARESİNİ ALMA
"""

def karesi_al(x):
    print("karesi= {}".format(x*x))

x = int(input("karesini almak istediginiz sayi degerini giriniz :"))

karesi_al(x)

"""







#İSTEDİGİMİZ SAYIYI İSTEDİGİMİZ DERECEDE ÜSTEL ALMA
"""

def us_al(alt,ust):
    print("sonuc: {}".format(alt**ust))

alt = int(input("taban degeri giriniz:"))

ust = int(input("us degeri giriniz:"))

us_al(alt,ust)

"""






#CLASS

"""
class Ucus():
    havayolu = "THY"

ucus1 = Ucus()

print(ucus1.havayolu)

"""







"""
class Ucus():
    havayolu = "THY"

    def __init__(self, kalkis, varis, sure, yolcu):
        self.kalkis = kalkis
        self.varis = varis
        self.sure = sure
        self.yolcu = yolcu

ucus1= Ucus("İST","USAK",50,333)

print(ucus1.varis)

"""







"""
class Ucus():
    havayolu = "THY"

    def __init__(self, kod, kalkis, varis, sure, kapasite, yolcu):
        self.kod = kod
        self.kalkis = kalkis
        self.varis = varis
        self.sure = sure
        self.kapasite = kapasite
        self.yolcu = yolcu

    def anons_yap(self):
        return "{} sayili {} {} seferi {} dakika surecektir".format(
            self.kod,
            self.kalkis,
            self.varis,
            self.sure,
        )

ucus3 = Ucus("TK1453","İST","USAK",64,300,246)

print(ucus3.anons_yap())

"""







# SEARCH VE SPAN KOMUTLARI


"""
cumle = " Mustafa Kemal Ataturk , Turk Asker,Turkiye Cumhuriyetinin Kurucusudur"

patern = "Turk"

print(re.search(patern,cumle))#türk kelimesinin başlangıç ve bitiş değerini gösterir

durum = re.search(patern,cumle)

print(durum.span()) #türk kelimesinin başlangıç ve bitiş değerini daha net gösterir

print(dir(durum))    #kullanılabilir komut listesini gösterir

print(durum.start())

print(durum.end())


for eslesme in re.finditer(patern,cumle):     #turk kelimesini geçtiği her yeri net gösterir
    print(eslesme.span(),eslesme.group())

"""








"""
ornek = "en sevdigim kanal 42istanbul"#bu cümleden

patern = "\d\distanbul" #bu kalıbı arıyoruz

print(re.search(patern,ornek)) #aratma kodu

"""







"""
ornek ="benim telefon numaram 0569-8529564268"

patern = "\d\d-\d\d\d\d\d\d\d\d\d\d"

print(re.search(patern,ornek))

durum=re.search(patern,ornek)

print(durum.span())
"""







#EN AZ 5 KARAKTERLİ KELİMELERİ BASTIRMA

"""
ornek = "en sevdigim kanal 42istanbul"

patern = "\s\w{5,}"  #en az karakterli kelimeler demek

for eslesme in re.finditer(patern,ornek):
    print(eslesme.group(),eslesme.span())
"""








#EN AZ BİR RAKAM VE YA DAHA FAZLA RAKAM OLAN KELİMELERİ ALAN FONKSİYON

"""
ornek = "en sevdigim kanal 42istanbul"

patern = "\d+" #EN AZ BİR RAKAM VE YA DAHA FAZLA RAKAM OLAN KELİMELERİ AL


for eslesme in re.finditer(patern,ornek):
    print(eslesme.group(),eslesme.span())
"""










#EN AZ BİR RAKAM VE YA DAHA FAZLA RAKAM OLAN VE SIFIR VE YA DAHA FAZLA KARAKTERLİ KELİMELERİ AL
"""
ornek = "en sevdigim kanal 42istanbul"

patern = "\d+\w*"#EN AZ BİR RAKAM VE YA DAHA FAZLA RAKAM OLAN VE SIFIR VE YA DAHA FAZLA KARAKTERLİ KELİMELERİ AL

for eslesme in re.finditer(patern,ornek):
    print(eslesme.group(),eslesme.span())

"""







"""
def gsm_operator(tel_no):

    patern = "(\d{3})-(\d{7})"
    eslesme = re.search(patern,tel_no)

    if eslesme:
        gsm_kod = eslesme.groups()[0]
        print(gsm_kod)

        if gsm_kod.startswith("542"):
            return "vodofone"
        elif gsm_kod.startswith("501"):
            return "avea"
        elif gsm_kod.startswith("535"):
            return "turkcell"
        else:
            return "sebeke hatası"


    else:
        return "patern hatası"


tel_no = "0535-5692459"

print(gsm_operator(tel_no))

"""








"""
 |  ve ya

 ^ baslar

 $ biter

 . herhangi

 \ esc

"""







"""
import random

#help(random)

print(random.random()) #0 ile 1 arasında rastgele sayı verir

print(random.uniform(4,9)) # 4 ile 9 arasnda rastgele sayı verir

print(random.randint(4,9)) # 4 ile 9 arasnda rastgele integer sayı verir

print(random.choice(range(10)))

print(random.sample(range(10),k=4)) #rastgele 4 deger verir

import math

print(math.ceil(7.1)) #üst degere yuvarlar

print(math.floor(7.8)) #alt degere yuvarlar

print(math.factorial(5)) #faktoriyel hesaplar

print(math.pow(3,4)) #üssü hesaplar

"""








"""
from collections import Counter

import random


list1 = random.sample(range(10),k=4)

list2 = random.sample(range(10),k=4)

list3 = random.sample(range(10),k=4)

list4 = random.sample(range(10),k=4)



lists = [list1,list2,list3,list4]

list_toplam = list1 + list2 + list3 + list4

print(lists)

print(list_toplam)


for index,liste in enumerate(lists):
    print("{} . liste \t {}".format(index,liste))

print(Counter(list_toplam)) #her karakterden kaç tane olduğunu söyler

print(Counter("asdfgasdfg"))  #örneğin

"""







# KARAKTERLERİN KAÇ TANE OLDUĞUNU GÖSTERİR
"""
from collections import Counter

soz = "gel git git gel gelmek gitmek gitmek gelmemek"

print(Counter(soz))

print(Counter(soz.split()))

"""








"""
from datetime import date

print(date.today())  # bugünün tarihini verir

bugun = date.today()  #bugünün tarihini bir başka şekilde verir
print(bugun)

dun = date(2022,7,13)   #girdiğin taarihi basar
print(dun)

print(bugun-dun)  #günler arasında zamanı verir

print(dun<bugun)  #dün bugünden daha geride mi sorusuna cevap verir

print(bugun.year)

print(bugun.month)

print(bugun.day)

print(bugun.__getattribute__("day"))

print(bugun.__getattribute__("year"))

print(bugun.__getattribute__("month"))

print(date.isocalendar(bugun)) #2022 37 2 output u çıkar anlamı ise 37 yılın 37. haftası 2 ise
#haftanınn 2.günü

print(date.weekday(bugun))  #bu komutta 0 pzrts  1 salı 2 çarşamba diye ilerler

print(date.ctime(bugun)) # hangi gün olduğu hangi ay olduğu ayın kaçıncı günü olduğu ve yıl döndürülür
"""






"""
from datetime import date
from datetime import time

print(time(23,19))

print(time(23,19,9))

zaman = time(22,15,57)
print(zaman.hour)
print(zaman.second)
print(zaman.minute)

dt= datetime.datetime(2022,7,13,22,15,45)
print(dt)
"""









# BİR İSLEMİ YAPARKEN NE KADAR SÜREDE YAPILDIĞI İLE BULMAK

"""
import time

def sure_olc(f):
    def wrapper(*args):

        baslangic = time.time()
        print("baslangic zamani : {}\t".format(baslangic))

        f(*args)

        bitis = time.time()
        print("bitis zamani : {}\t".format(bitis))
        print("gecen zaman : {}\t".format(bitis-baslangic))

    return wrapper


# faktoriyel = 5*4*3*2*1 = 120

@sure_olc
def faktoriel(sayi):

    toplam = 1
    while sayi > 1:
        toplam = toplam * sayi
        sayi = sayi-1

    print("faktoriyel sonucu : {}".format(toplam))

faktoriel(999)

"""









"""
import requests

bolge_URL = "https://data.police.uk/api/crime-categories?date=2011-08 "  #http://www.webcode.me  #https://data.police.uk/api/force

response = requests.get(bolge_URL)

#help(response) #bu komut ile nasıl kullanılacağı öğrenilir

print(response.status_code)

print(response.url)

print(response.text)
"""










"""
import requests

suc_kategori_URL = "https://data.police.uk/api/crime-categories "

payload = {"date" : "2011-09"}

response = requests.get(suc_kategori_URL,params=payload)

print(response.status_code)

print(response.url)

print(response.json()) #bu komut ile url ye ait sayfadaki kategoriler çıktısı verilir
"""









#SİTEEKİ DATALARA ULAŞMA
"""
import requests

suc_url = "https://data.police.uk/api/crimes-no-location"
#?category=all-crime&force=leicestershire&date=2017-03"
payload = {
    "category" : "all-crime",
    "force" : "city-of-london",
    "date" : "2020-03"
}

response = requests.get(suc_url,params=payload)

print(response.text)

print(list(response.text))
"""




#uygulama python dersleri 39.video son 10 dk incele

#C:\Users\T.c.severoğlu\PycharmProjects\pythonProject1\venv\Scripts\python.exe -m pip install --upgrade pip

#from PIL import Image

#from io import BytesIO

#import requests

#grafik_url = "https://image-charts.com/chart"

#chco=3092de%2C027182&chd=t%3A81%2C65%2C50%2C67%2C59%7C77%2C67%2C10%2C79%2C65&chdl=First%7CSecond&chdlp=b&chs=480x480&cht=r&chxt=r

#payload = {
   # "chco":"3092de%2C027182",
   # "chd" : "t%3A81%2C65%2C50%2C67%2C59%7C77%2C67%2C10%2C79%2C65",
   # "chdl" : "First%7CSecond",
   # "chdlp":"b",
   # "chs":"480x480",
   # "cht":"r",
   # "chxt":"r"
#}
#response = requests.post(grafik_url , data=payload)

#print(response.status_code)

#print(response.content)


#image = Image.open(BytesIO(response.content))

#image.show()






"""

from tkinter import *
from tkcalendar import DateEntry


master = Tk()

canvas = Canvas(master,height=450,width=750)  #ekranın büyüklüğünü ayarlar
canvas.pack()

frame_ust = Frame(master,bg="yellow")
frame_ust.place(relx=0.1, rely=0.1, relwidth=0.75, relheight=0.1)

frame_sol = Frame(master,bg="yellow")
frame_sol.place(relx=0.1, rely=0.3, relwidth=0.3, relheight=0.5)



master.mainloop()
"""









"""
from tkinter import *
from tkcalendar import DateEntry
from tkinter import messagebox


master = Tk()

canvas = Canvas(master,height=500,width=750)  #ekranın büyüklüğünü ayarlar
canvas.pack()

#FRAME_UST EN USTTEKİ SARI BOLGE ANLAMINA GELİR RELX RELY VS GİBİ TERİMLER İLE SARI BOLGE DOLDURULUR
frame_ust = Frame(master,bg="yellow")
frame_ust.place(relx=0.1, rely=0.1, relwidth=0.75, relheight=0.1)

frame_sol = Frame(master,bg="yellow")
frame_sol.place(relx=0.1, rely=0.25, relwidth=0.4, relheight=0.5)

frame_sag = Frame(master,bg="yellow")
frame_sag.place(relx=0.55, rely=0.25, relwidth=0.4, relheight=0.5)

#HATIRLATMA ETİKET SARI BOLGENİN UZERİNE YAZILAN YAZILARI BELİRTİR LABEL ETİKET ANLAMINA GELİR
hatirlatma_etiket = Label(frame_ust, bg="#BFBFBF", text="HATIRLATMA TİPİ :",font="verdana 10 bold")
hatirlatma_etiket.pack(padx=10, pady=10,side=LEFT)
#PADX VE PADY AYNI FRAME UST BLOGUNDA OLDUĞU GİBİ YAZININ YERİNİ BELİRLER

hatirlatma_opsiyon = StringVar(frame_ust)
hatirlatma_opsiyon.set("\t")


hatirlatma_acilir = OptionMenu(
    frame_ust,
    hatirlatma_opsiyon,
    "Birthday",
    "Weddind Day",
    "Pay"

)
hatirlatma_acilir.pack(padx=10, pady=10,side=LEFT)

hatirlatma_tarih = Label(frame_ust, bg="#BFBFBF", text="TARİH :",font="verdana 10 bold")
hatirlatma_tarih.pack(padx=10, pady=10, side=LEFT)

hatirlatma_tarih_secici = DateEntry(frame_ust,background = "pink",foreground = "yellow",borderwith=1,locale="de_DE")
hatirlatma_tarih_secici._top_cal.overrideredirect(False)
hatirlatma_tarih_secici.pack(padx=5, pady=10,side=RIGHT)

#BU YAZIM TİPİ KISA HALİ EN SON .PACK DİYEREK İŞLEMİ BİTİRİYORUZ VE ANCHOR KONUMU BELİRTİR NW MESELA NORTH EST DEMEK
Label(frame_sol,text="HATIRLATMA SEÇENEKLERİ",bg="#add3e9",font="verdana 10 bold").pack(pady=10,padx=10,anchor=NW)


#ANA SEÇENKLERİN OLDUĞU KOD YERİ
var= IntVar()

R1 = Radiobutton(frame_sol,text= "sisteme kaydet",variable=var,value=1,bg="#add3e9",font="verdana 10").pack(anchor=NW,pady=5,padx=15)

R2 = Radiobutton(frame_sol,text= "e-posta gonder",variable=var,value=2,bg="#add3e9",font="verdana 10").pack(anchor=NW,pady=5,padx=15)



#alt seçenekleri belirtmek için kullanılan kod mantığı
#mesela
# DOĞUM GÜNÜ --> ana başlık
#      -günü
#      -ayı    -----> bunlar ise alt başlık bu alt başlıkların kodu aşağıdadır
#      -yılı

#BİRİNCİ ALT BAŞLIK
var1= IntVar()
E1 = Checkbutton(frame_sol,text="bir ay once",variable=var1,onvalue=1,offvalue=0,bg="#add3e9",font="verdana 10").pack(anchor=NW,pady=5,padx=35)

#İKİNCİ ALT BAŞLIK
var2= IntVar()
E2 = Checkbutton(frame_sol,text="bir hafta once",variable=var2,onvalue=1,offvalue=0,bg="#add3e9",font="verdana 10").pack(anchor=NW,pady=5,padx=35)

#ÜÇÜNCÜ ALT BAŞLIK
var3= IntVar()
E3 = Checkbutton(frame_sol,text="bir gun once",variable=var3,onvalue=1,offvalue=0,bg="#add3e9",font="verdana 10").pack(anchor=NW,pady=5,padx=35)


#KULLANICININ SAVE ETMESİ İÇİN KONULAN TUŞUN ÇALIŞMASI İÇİN FONKSİYON
def save():
    son_mesaj = ""#son mesaj diye bir eleman tanımladık bu ekrana info olarak çıkacak yazıdır

    #var .get ile alt başlıklara özgü kodlar yazılır
    if var.get():
        if var.get() == 1:  #ilk seçenek yani sisteme kaydet seçilir ise çalışacak kod
            son_mesaj += "Sisteme kaydedilmiştir."

#bilgisayara kaydetmeye yarayan kullanıcının kaydet dediği notları gerçekten kaydetmeye yarayan kod bloğu
            tip = hatirlatma_opsiyon.get() if hatirlatma_opsiyon.get() == "" else "Genel"
            tarih = hatirlatma_tarih_secici.get()
            mesaj = text_alani.get("1.0","end")

#haturlatmalar adında bir text dosyası oluşturulur ve dosyanın içine yazılacak bilgiler aktarılır
            with open("hatirlatmalar.txt","w") as dosya:
                dosya.write(
                "{} kategorisinde {} tarihine {} notuyla hatırlatma".format(tip,tarih,mesaj))
                dosya.close()

#eğer kullanıcı ikinci yani eposta yolunu seçer ise çalışcak kod bloğu
        elif var.get() == 2:
            son_mesaj += "E-posta ile kayıt sağlanmıştır"

        messagebox.showinfo("Başarılı işlem ",son_mesaj)
    return


#SAĞ TARAFTAKİ BÖLÜM İÇİN ETİKET
Label(frame_sag,text="HATIRLATMA MESAJI",bg="#add3e9",font="verdana 10 bold").pack(padx=5,pady=5,anchor=NW)


#KULLANICIN NOT LALABİLMESİ İÇİN VERİLEN TEXT ALANI
text_alani = Text(frame_sag,height=11,width=35)
text_alani.tag_configure("style", foreground="#8B8878", font=("verdana",7,"bold"))
text_alani.pack()


#KULLANICININ O ALANA(TEXT ALANI) NE YAZMASI GEREKTİĞİNİ ANLAMASI İÇİN BİR NOT DÜŞME
karsilama_metni = "Mesajınızı giriniz.."
text_alani.insert(END,karsilama_metni,"style",)


#KULLANICININ YAZDIĞI NOTU KAYDETMESİ İÇİN BİR TUŞ
save_button = Button(frame_sag,text="SAVE",command=save,).pack(anchor=S)



master.mainloop()
"""






"""
#BASİT BİR ŞEKİLDE E POSTA GÖNDERİMİ(GÖNDERİLMESİ İÇİN BELİRLİ İİZNLERİN VERİLİYOR OLMASI LAZIM)
#DERS 46 SON DKLAR ANLATIYOR

import ssl
import smtplib

kullanici = "denemeemre220@gmail.com"
sifre = "EmreDeneme963258"

alici = kullanici
baslik = "ANA BAŞLIK"
mesaj = "neaptın"

context = ssl.create_default_context()

port = 465
host = "smtp.gmail.com"

eposta_sunucu = smtplib.SMTP_SSL(host=host, port=port, context=context)
eposta_sunucu.login(kullanici, sifre)
eposta_sunucu.sendmail(kullanici, alici, mesaj)



from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders



posta = MIMEMultipart()

posta["from"] = kullanici
posta["to"] = kullanici
posta["subject"] = baslik

posta.attach(MIMEText(mesaj,"plain"))
eklenti_dosya_ismi = "foto.jpg"

with(open(eklenti_dosya_ismi,"rb")) as eklenti_dosyasi:
    payload = MIMEBase("application","octate-stream")
    payload.set_payload((eklenti_dosyasi).read())
    encoders.encode_base64(payload)

    payload.add_header("Content-Decomposition","attachment",eklenti_dosya_ismi)
    posta.attach(payload)

    posta_str = posta.as_string()


port = 465
host = "smtp.gmail.com"

eposta_sunucu = smtplib.SMTP_SSL(host=host, port=port, context=context)
eposta_sunucu.login(kullanici,sifre)
eposta_sunucu.sendmail(kullanici, alici, posta_str)

"""

"""
#from imap_tools import Mailbox

#47. video yarım bıraktım bilgisayar hata veriyor

import matplotlib.pyplot as plt
import ipywidgets as widgets
import pandas as pd
import numpy as np
from io import StringIO
import matplotlib.pyplot as plt
#%matplotlib inline
#from pandas.compat import StringIO

tab = widgets.Tab()
placeholder = widgets.Label()
tab.children = [placeholder,placeholder,placeholder]
tab.set_title(0 , "Upload")
tab.set_title(1 , "Describer")
tab.set_title(2 , "Plotter")
tab


up = widgets.FileUpload(accept ="" ,multiple=False)
up


out = widgets.Output(layout={"border" : "lpx solid black"})
tab.children = [up,out,out]
tab


eraser = widgets.SelectMultiple(
    options = ["tab",'""'],
    value = ["tab"],
    description = "Eraser: ",
    disabled = False
)
eraser


delim = widgets.RadioButtons(
    options = [";" , "," , " "],
    description = 'separator: ',
    disabled = False
)
delim


rows = widgets.IntSlider(
    value = 0,
    step =1,
    description = "#of lines: ",
    disabled = False,
    continious_update = False,
    orientation = "horizontal",
    readout = True,
    readout_format = "d"
)
rows
"""







# QR KOD OKUYUCU
"""
import cv2
import webbrowser

cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()

while True:

    _,img = cap.read()
    data,one, _= detector.detectAndDecode(img)
    if data:
        link=data
        break
    cv2.imshow("QR Code Reader",img)
    if cv2.waitKey(1)==ord("q"):
        break

b=webbrowser.open(str(link))
cap.release(link)
cv2.destroyAllWindows

"""


"""
from keplergl import KeplerGl

map = KeplerGl(height =900)
map

"""



"""
import pywhatkit as kit

try:
    kit.sendwhatmsg("+90xxxxxxxxx","a \U0001F607",14,25)
    print("basarili")
except:
    print("olmadi")

"""



