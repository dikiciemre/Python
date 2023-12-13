"""
#input alma

sayi=input("sayi girisi yapiniz")
print("Sayi {} degerine esittir".format(sayi) )

"""





# ARİTMETİK İŞLEM YAPTIRMA
"""
print("ARİTMETİK İŞLEM YAPTIRMA\n")  # ARİTMETİK İŞLEM YAPTIRMA

print("Yapmak istediğiniz işlemi seçiniz:\n 1-TOPLAMA\n 2-ÇIKARMA\n------------------")
select = input("seçilen işlem :")

print("işlem yapmak istediğiniz sayıları giriniz..")
sayi1 = input('sayi1 :')
sayi2 = input('sayi2 :')

    if (select == 1):
         sonuc = sayi2 + sayi1
         print("\ntoplama işlemini seçtiniz..\n sonuc: {} ".format(sonuc))

    elif (select == 2):
         sonuc = sayi2 - sayi1
         print("\nçıkarma işlemini seçtiniz..\n sonuc: {} ".format(sonuc))

    else:
         print("\nsg burdan")

"""









# NOT HESAPLAMA
"""
vizeNotu1 = float(input("1. Vize notu gir : "))
vizeNotu2 = float(input("2. Vize notu gir : "))
finalNotu = float(input("Final notu gir :"))

genelOrtalama = (((vizeNotu1 + vizeNotu2) / 2) * 0.4) + (finalNotu * 0.6)

print("Not ortalamanız : ", genelOrtalama)



if finalNotu >= 50:

    if (genelOrtalama >= 85 and finalNotu >= 50):
            print("Harf Notunuz AA")
    elif genelOrtalama >= 75 and genelOrtalama < 85:
            print("Harf Notunuz BA")
    elif genelOrtalama >= 70 and genelOrtalama < 75:
            print("Harf Notunuz BB")
    elif genelOrtalama >= 65 and genelOrtalama < 70:
            print("Harf Notunuz CB")
    elif genelOrtalama >= 60 and genelOrtalama < 65:
            print("Harf Notunuz CC")
    elif genelOrtalama >= 55 and genelOrtalama < 60:
            print("Harf Notunuz DC")
    elif genelOrtalama >= 50 and genelOrtalama < 55:
            print("Harf Notunuz DD")

else:
        print("Harf notunuz FF kaldınız .")
"""






#girilen 3 sayıyı sıralama algoritması
"""

print("girilen 3 sayıyı sıralama algoritması..\n------------------------------------")

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

if (a > b) and (a > c):
	print(a, "en büyük sayıdır.")

elif (b > a) and (b > c):
	print(b, "en büyük sayıdır.")

elif (c > a) and (c > b):
	print(c, "en büyük sayıdır.")

else:
    print("kime baktın birader")
    
"""






#hava durumu bilgisine göre tavsiye veren program
"""
print("hava durumu bilgisine göre tavsiye veren program\n")

hava_durumu = input("SEÇENEKLER: 1-gunesli 1-yagmurlu \nhava durumu şu an nasıl ?")

if(hava_durumu == "gunesli"):
    tercih = input("1-şapka 2-su \nhangisini seçmek istersiniz ?..")

    if(tercih == 1):
        print("hava durumu güneşli ve şapka tercih ettiniz..\ngötün yanacak aq dur evde")
    elif(tercih == 2):
        print("hava durumu güneşli ve su tercih ettiniz..\nsu iyidir aferin..")
    else:
        print("hatalı giriş")

elif(hava_durumu == "yagmurlu"):
    tercih = input("1-şemsiye 2-bot \nhangisini seçmek istersiniz ?..")

    if (tercih ==1):
        print("hava durumu yağmurlu ve şemsiye tercih ettiniz..\nayağın  üşücek aq dur evde")
    elif (tercih ==2):
        print("hava durumu yağmurlu ve bot tercih ettiniz..\nbot iyidir aferin..")
    else:
        print("hatalı oldu")
else:
    print("sistem kapalı!!!!!!")
"""












