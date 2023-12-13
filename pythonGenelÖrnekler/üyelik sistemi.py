import json
import random
from os import system

#ÇALIŞMIYORRRRR!!!!!!!!!!!!!!!!!!!!!!!!!!!!



class System():
    def duzenle(self, veriler):
        h = input("Kullanıcı adınızı giriniz: ")
        with open("kullanıcılar.json", "r+") as dosya:
            falan = json.load(dosya)
        for x in falan["kullanici"]:
            if h == x["kadi"]:
                a = str(random.randint(1000000, 99999999))
                with open("aktivasyonum.txt", "w+") as dosia:
                    dosia.write(a)
                b = input("Aktivasyon kodunu giriniz: ")
                if b == a:
                    s = int(input(
                        "Hesap bilgilerini görüntülemek için 1, hesap bilgilerini değiştirek için 2, ana sayfaya dönmek için 3 yazınız: "))
                    if s == 1:
                        print("""
Kullanıcı adı: {z}                    
Şifre: {c}
E-posta: {s}                    
""".format(z=x["kadi"], c=x["sifre"], s=x["eposta"]))
                        input("Ana sayfaya dönmek için herhangi bir tuşa basınız.")
                    elif s == 2:
                        with open("kullanıcılar.json", "r+") as dosya:
                            falan = json.load(dosya)
                            a = input(
                                "Kullanıcı adınızı giriniz (Değiştirmek istemiyorsaız aynı kullanıcı adını giriniz.): ")
                            for i in a:
                                bum = ["a", "b", "c", "d", "e", "f", "g", "ğ", "ı", "i", "j", "k", "l", "m", "n", "o",
                                       "ö",
                                       "p", "r",
                                       "s", "ş", "t", "u", "ü", "v", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8",
                                       "9",
                                       "0", ".", "x", "q", "w", "_"]
                                if not i in bum:
                                    print(
                                        "^^,#,' gibi değerler ve büyük harf, kullanıcı adı için kullanılamaz. Tekrar deneyiniz.")
                                    self.kayitol()
                        vv = input("E-posta adresinizi giriniz (Değiştirmek istemiyorsaız aynı e-postayı giriniz.): ")
                        if not "@" in vv:
                            print("Geçersiz bir e-posta adres girdiniz. Tekrar deneyiniz.")
                            self.kayitol()
                        for i in vv:
                            bum = ["a", "b", "c", "d", "e", "f", "g", "ğ", "ı", "i", "j", "k", "l", "m", "n", "o", "ö",
                                   "p", "r",
                                   "s", "ş", "t", "u", "ü", "v", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                                   "0", ".",
                                   "x", "q", "w", "_"
                                                  "A", "B", "C", "D", "E", "F", "G", "Ğ", "I", "İ", "J", "K", "L", "M",
                                   "N", "O", "Ö", "P", "R",
                                   "S", "Ş", "T", "U", "Ü", "V", "Y", "Z", "X",
                                   "Q", "W", "@"]
                            if not i in bum:
                                print("^^,#,' gibi değerler, e-posta için kullanılamaz. Tekrar deneyiniz.")
                                self.kayitol()
                        ss = input("Şifre giriniz (Değiştirmek istemiyorsaız aynı şifreyi giriniz.): ")
                        for i in ss:
                            bum = ["a", "b", "c", "d", "e", "f", "g", "ğ", "ı", "i", "j", "k", "l", "m", "n", "o", "ö",
                                   "p", "r",
                                   "s", "ş", "t", "u", "ü", "v", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                                   "0", ".", "x", "q", "w", "_",
                                   "A", "B", "C", "D", "E", "F", "G", "Ğ", "I", "İ", "J", "K", "L", "M", "N", "O", "Ö",
                                   "P", "R",
                                   "S", "Ş", "T", "U", "Ü", "V", "Y", "Z", "X", "Q", "W"]
                            if not i in bum:
                                print("^^,#,' gibi değerler, şifre için kullanılamaz. Tekrar deneyiniz.")
                                self.kayitol()
                        if a == ss:
                            print("Kullanıcı adı ve şifre aynı olamaz. Tekrar deneyiniz.")
                            self.kayitol()
                        if ss == "":
                            print("Geçersiz şifre tekrar deneyiniz.")
                            self.kayitol()
                        else:
                            with open("kullanıcılar.json", "r+") as dosya:
                                falan = json.load(dosya)
                                veriler["kullanici"].append({"kadi": f"{a}", "sifre": f"{ss}", "eposta": f"{vv}"})
                        with open("kullanıcılar.json", "r+") as dosya:
                            json.dump(veriler, dosya)
                        print("Düzenleme işlemi gerçekleştirildi.")
                        input("Ana sayfaya dönmek için herhangi bir tuşa basınız.")
                        self.calistir()
                    elif s == 3:
                        pass
                    else:
                        print("Hatalı seçim. Tekrar deneyiniz.")
                        self.duzenle()
                else:
                    input("Doğrulama kodunu yanlış girdiniz. Yeniden denemek için herhangi bir tuşa basınız.")
        else:
            print("Geçersiz kullanıcı adı tekrar deneyiniz.")
            self.calistir()

    def cikis(self):

        print("İyi günler.")

    exit()

    def hata(self):

        input(
            "Şifreyi yanlış girdiniz. Şifreyi ana sayfadan değiştirebilirsiniz. Ana sayfaya dönmek için herhangi bir tuşa basınız.")
        self.calistir()

    def calistir(self):

        while True:
            print("""
Kullanıcı İşlemleri:
1) Giriş yap.
2) Kayıt ol.
3) Hesap bilgileri ve hesap işlemlerini görüntüle.
4) Çıkış.
""")
            t = int(input("Yapmak istediğiniz işlemin numarasını giriniz: "))
            if t == 1:
                self.giris()
            elif t == 2:
                self.kayitol()
            elif t == 3:
                self.duzenle()
            elif t == 4:
                self.cikis()
            else:
                print("Yanlış bir değer girdiniz tekrar deneyiniz.")
                continue



