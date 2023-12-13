import numpy as np


# numpy ile array oluşturmak hepsi aynı tip olmalı
#array = np.array([1,2,3,4]); print(array)


# dtype ile dizini tipini integer seçtik 4.6 yı 4 e dönüştürdü
#array1 = np.array([1,2,3,4,4.6], dtype=int) ;  print(array1)


# 3 e 4 lük matris yapar
#aray = np.zeros((3,4)); print(aray);


# 3 tane 4 e 2 lik matris
#aray = np.zeros((3,4,2)); print(aray);



# 3 e 4 lük bir matrisi 2 ler ile doldurur
#a = np.full((3,4),2);  print(a)




# 0 dahil 10 dahil değil bir matris oluşturur
#print(  np.arange(0,10)  )




# linspace default olarak 50 tane noktayı 1 ve 2 dahil olarak matris üretir
#print( np.linspace(1,2) )




# eşit 4 aralığa böler
#print( np.linspace(1,2, num = 4) )




# 3 e 4 bir matrisi 1 ile 10 arasındaki rakamlar ile random oluşturur
#print( np.random.randint(1,10,(3,4)))




# birim matris oluşturma kare matris vermez isek(5*4 ,8*2, 3*9 gibi) diagonal değerleri 1 ile doldurur
#print( np.eye(5,4))



# bu eşkilde direkt çarpamaz
#a = [1,2,3];   b = [2,3,4];  print(a*b);



#her değeri 3 ile çarpmaz diziyi 3 kere yan yana yazar  [1, 2, 3, 1, 2, 3, 1, 2, 3]
#a = [1,2,3]; print(a*3)



# dizi değerlerini çarpar   [ 4  9 16]
#a = np.array([2,3,4]);   b = np.array([2,3,4]);  print(a*b);



# değerleri 3 ile çarpar   [3 6 9]
#a = np.array([1,2,3]);   print(a*3)



#dizinin kaça kaçlık olduğunu belirtir (3, 4, 2)
#aray = np.zeros((3,4,2));  print(aray.shape)




# n dimentionunu verir  2
#aray = np.zeros((3,4)); print(aray);  print(aray.ndim)



# n dimentionunu verir  3
#aray = np.zeros((3,4,5)); print(aray);  print(aray.ndim)





# kaç elemanlı olduğunu  verir  12
#aray = np.zeros((3,4)); print(aray);  print(aray.size)




# kaç elemanlı olduğunu  verir  60
#aray = np.zeros((3,4,5)); print(aray);  print(aray.size)



# reshape ile diziyi istediğin formata dönüştürür
# [[0 1 2 3 4]
#  [5 6 7 8 9]]
# a = np.arange(0,10);  print(a.reshape(2,5))




#iki diziyi birleştirir
#array = np.array([1,2,3,4]);    array1 = np.array([4,5,6,7,8,9]);  print(np.concatenate([array,array1]));





# kolon mantığında birleştirme yapar ancak iki dizininde boyutları ayn olmalı
#array = np.array([1,2,3,4]);    array1 = np.array([6,7,8,9]); print(np.stack([array,array1]));






# ilk 2 terimi bir array 2-5. terimleri bir array geri kalanları da ayrı bir array yapar  [array([10, 20]), array([30, 40, 50]), array([60, 70])]
#a = [10,20,30,40,50,60,70];   print(np.split(a,(2,5)))






#küçükten büyüğe sıralar
#array = np.array([20,3,5,56,89,12]);  print(np.sort(array))




#[[ 1  2  3  4  5]
# [ 6  7  8  9 10]
# [11 12 13 14 15]
# [16 17 18 19 20]]

#a = np.arange(1,21).reshape(4,5);  print(a,"\n");
#print(a[0]) #1.row u getirir  [1 2 3 4 5]
#print(a[0].ndim)
#print(a[0,0]) #1. row 1. column verir
#print(a[2,3]) #3. row 4. column verir  14
#a[1,1] = 10;  print(a); # 2. row 2.columndaki değeri 10 ile değiştirir






#index listesine attığı değerleri a dizisinden seçer ve bastırır  [ 5  6  8 14]
#a = np.arange(1,15); print(a); index = [4,5,7,13];   print(a[index])






#a = np.arange(1,13).reshape(3,4); print(a,"\n");
#b = a[:2,:3]; print(b,"\n");
#b[0,0]=100; print(b,"\n")








#a = np.arange(1,13).reshape(3,4); print(a,"\n");
#print(np.sum(a))  # matrisin tüm değerlerini toplar
#filt = a < 5;  print(filt); # filtre tanımlandı ve matriste 5 den küçük olan değerler true ile belirtildi.
#print(a[filt]) # filtrenin sağladığı değerleri bastırır  [1 2 3 4]
#print(np.sum(a,axis=0)) # değerleri dikey olarak toplar ve yazar
#print(np.sum(a,axis=1)) # değerleri yatay olarak toplar ve yazar






