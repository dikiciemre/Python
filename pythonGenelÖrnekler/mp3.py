

import random

class Mp3calar ():
    def __init__(self):
        self.sarkilar = []
        self.calansarki = ""
        self.sesduzeyi = 50
        self.mp3durumu = True
        self.kacsarkivar = 0
        self.controller()
        self.anamenu()


    def controller (self):
        if self.calansarki == "":
            self.calansarki = "Şarkı Çalmıyor"
        if self.calansarki not in self.sarkilar:
            self.calansarki = "Şarkı Çalmıyor"


    def anamenu (self):
        print("****/MP3 Çalara Hoşgeldiniz\****")
        while (self.mp3durumu):
            self.controller()
            print(f"""     
Şarkılar: {self.sarkilar}
Çalan Şarkı: {self.calansarki}
Ses Düzeyi: {self.sesduzeyi}

1-Şarkı Ekle
2-Şarkı Sil
3-Şarkı Seç
4-Rastgele Şarkı Seç
5-Ses Arttır
6-Ses Azalt
7-Şarkıyı kapat
8-Kapat

""")
            self.menusec = int(input("Yapmak istediğiniz işlemin yanındaki numarayı giriniz: "))

            if self.menusec == 1:
                print("")
                self.sarkiekle = input("Lütfen şarkı ismini giriniz: ")
                self.sarkilar.append(self.sarkiekle)
                self.kacsarkivar += 1
                print("Şarkı başarıyla eklendi")


            if self.menusec == 2:
                if len(self.sarkilar) <= 0:
                    print("Şarkınız bulunmamakta")
                else:
                    print("")
                    id = 1
                    sarkilarinuzunlugu = len(self.sarkilar)

                    for i in range(0,sarkilarinuzunlugu):
                        print(f"{id}) {self.sarkilar[i]}")
                        id += 1
                    print("")
                    self.sarkisil = int(input("Lütfen şarkının yanındaki numarayı yazınız: "))

                    if self.sarkisil > len(self.sarkilar):
                        print("")
                        print("Lütfen geçerli bir sayı giriniz!")
                    elif self.sarkisil <= 0:
                        print("")
                        print("Lütfen geçerli bir sayı giriniz")
                    else:
                        self.sarkilar.pop(self.sarkisil -1)
                        print("")
                        print("Şarkı başarıyla silindi")

            if self.menusec == 3:
                if len(self.sarkilar) <= 0:
                    print("Şarkınız bulunmamakta")
                else:
                    print("")
                    id = 1
                    sarkilarinuzunlugu = len(self.sarkilar)

                    for i in range(0,sarkilarinuzunlugu):
                        print(f"{id}) {self.sarkilar[i]}")
                        id += 1
                    print("")

                    self.sarkisec = int(input("Lütfen seçmek istediğiniz şarkının yanındaki numarayı giriniz: "))

                    if self.sarkisec > len(self.sarkilar):
                        print("")
                        print("Lütfen geçerli bir sayı giriniz!")
                    elif self.sarkisec <= 0:
                        print("")
                        print("Lütfen geçerli bir sayı giriniz")
                    else:
                        self.calansarki = self.sarkilar [self.sarkisec -1]
                        print("")
                        print("Şarkı seçildi")

            if self.menusec == 4:
                if self.kacsarkivar >= 2:

                    self.rastgelesarkisec = random.choice(self.sarkilar)

                    self.calansarki = self.rastgelesarkisec
                    print("")
                    print(f"Rastgele seçilen şarkı: {self.calansarki}")

                else:
                    print("")
                    print("Rastgele şarkı seçmek için 2'den fazla şarkınızın olması lazım!")

            if self.menusec == 5:
                if self.sesduzeyi >= 100:
                    print("")
                    print("Ses düzeyi zaten MAX Durumda")
                else:
                    self.sesduzeyi += 10
                    print("")
                    print("Ses arttırıldı")

            if self.menusec == 6:
                if self.sesduzeyi <= 0:
                    print("")
                    print("Ses düzeyi zaten MIN Durumda")
                else:
                    print("")
                    print("Ses arttırıldı")

            if self.menusec == 7:
                if self.calansarki == "" or self.calansarki == "Şarkı Çalmıyor":
                    print("")
                    print("Zaten şarkı çalmıyor")
                else:
                    self.calansarki = "Şarkı Çalmıyor"
                    print("")
                    print("Şarkı durduruldu")

            if self.menusec == 8:
                self.mp3durumu = False






mp3calar = Mp3calar

mp3calar()