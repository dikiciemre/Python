""""
a = 10

while(a > 0):

    print(a, ": Burası döngünün içi")
    a -= 1


print("Burası döngünün dışı")

"""







"""
istenilen = input("Yazdırmak istediğiniz değeri giriniz :")
adet = int(input("Kaç kere yazdırmak istediğinizi giriniz : "))


sira_no = 1

while(adet > 0):

	print(str(sira_no) + ". " + istenilen)
	adet -= 1
	sira_no += 1

"""







#0 DAN 100 E KADAR OLAN TÜM SAYILARIN HANGİSİ TEK HANGİSİ ÇİFT OLDUĞUNU GÖSTEREN PROGRAM
"""
x = 1

while x <= 100:

    if x % 2 == 1:
        print(f'sayı tek: {x}')

    else:
        print(f'sayı çift: {x}')
    x += 1

print('bitti...')

"""







"""
x = 0

while x < 5:

   x+=1

   if x == 2:
       break

   print(x)

"""









