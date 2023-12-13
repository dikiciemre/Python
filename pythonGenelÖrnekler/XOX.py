import os

class XOX():

    def __init__(self):

        self.ilk_işlemler()

        self.oyunu_baslat()


    def ilk_işlemler(self):

        self.tahta = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.oyuncu = 1  # Oyun 1.Oyuncu ile başlayacak.
        # Oyun Durumları
        self.Galibiyet = 1
        self.Beraberlik = -1
        self.Devam = 0
        #################

        self.Oyun = self.Devam  # Oyun ilk olarak devam ile başladı.
        self.İşaret = 'X'  # Sıra birinci oyuncuda olduğu için işaret X.

    def tahtayı_çiz(self):  # Bu fonksiyon her turda oyun tahtasını tekrar çizmemizi sağlayacak.
        os.system(
            'cls')  # Bu fonksiyon bir önceki çizdiğimiz tahtayı temizler, böylece konsolda kalabalık yapmış olmayız.

        print("   |   |   ")
        print(" {} | {} | {} ".format(self.tahta[1], self.tahta[2], self.tahta[3]))
        print("___|___|___")
        print("   |   |   ")
        print(" {} | {} | {} ".format(self.tahta[4], self.tahta[5], self.tahta[6]))
        print("___|___|___")
        print("   |   |   ")
        print(" {} | {} | {} ".format(self.tahta[7], self.tahta[8], self.tahta[9]))
        print("   |   |   ")

        # Burada yaptığımız işlem tamamen görünüş amaçlı.
        # Satır ve sütunları belli eden çizgiler ve onların arasına tahtamızdaki değerleri yazdırdık.
        # Kodu çalıştırdığımıza bunu daha iyi anlayabilirsiniz.

    def boşluk_kontrol(self, x):  # Bu fonksiyon tahtadaki bir hücrenin boş olup olmadığını kontrol edecek.

        if (self.tahta[x] == ' '):
            return True
        else:
            return False

    def durum_kontrol(self):  # Bu fonksiyon ise galibiyet, beraberlik ve devam durumlarını kontrol edecek.

        # Yatay Galibiyet Kontrolü
        if (self.tahta[1] == self.tahta[2] and self.tahta[2] == self.tahta[3] and self.tahta[1] != ' '):
            # Eğer 1., 2. ve 3. hücre birbirine eşitse ve boşluğa eşit değillerse bir oyuncu oyunu kazanmış demektir.

            self.Oyun = self.Galibiyet  # Eğer bir oyuncu oyunu kazanırsa başlangıçta devam olarak tanımladığımız Oyun değeri artık galibiyet olacak.

        # Diğer durumlarda az önce anlattığımızın aynısı olduğu için tekrar anlatmayacağız.
        elif (self.tahta[4] == self.tahta[5] and self.tahta[5] == self.tahta[6] and self.tahta[4] != ' '):
            self.Oyun = self.Galibiyet

        elif (self.tahta[7] == self.tahta[8] and self.tahta[8] == self.tahta[9] and self.tahta[7] != ' '):
            self.Oyun = self.Galibiyet

            # Dikey Galibiyet Kontrolü
        elif (self.tahta[1] == self.tahta[4] and self.tahta[4] == self.tahta[7] and self.tahta[1] != ' '):
            self.Oyun = self.Galibiyet

        elif (self.tahta[2] == self.tahta[5] and self.tahta[5] == self.tahta[8] and self.tahta[2] != ' '):
            self.Oyun = self.Galibiyet

        elif (self.tahta[3] == self.tahta[6] and self.tahta[6] == self.tahta[9] and self.tahta[3] != ' '):
            self.Oyun = self.Galibiyet

            # Çapraz Galibiyet Kontrolü
        elif (self.tahta[1] == self.tahta[5] and self.tahta[5] == self.tahta[9] and self.tahta[5] != ' '):
            self.Oyun = self.Galibiyet

        elif (self.tahta[3] == self.tahta[5] and self.tahta[5] == self.tahta[7] and self.tahta[5] != ' '):
            self.Oyun = self.Galibiyet

        elif (self.tahta[1] != ' ' and self.tahta[2] != ' ' and self.tahta[3] != ' ' and self.tahta[4] != ' ' and
              self.tahta[5] != ' ' and self.tahta[6] != ' ' and self.tahta[7] != ' ' and self.tahta[8] != ' ' and
              self.tahta[9] != ' '):

            # Eğer yukarıdaki durumların hiçbiri tutmadıysa ve tüm hücreler doluysa oyun berabere bitmiş demektir.
            self.Oyun = self.Beraberlik

        else:
            # Eğer oyunda bir kazanan yoksa ve beraberlikte yoksa oyun hala devam ediyordur.
            self.Oyun = self.Devam

    def oyunu_baslat(self):

        print("\n --- XOX Oyununa Hoş Geldiniz --- \n")

        oyuncu_1 = input("1.oyuncunun adını giriniz: ")
        oyuncu_2 = input("2.oyuncunun adını giriniz: ")

        print(f"{oyuncu_1} [X] --- {oyuncu_2} [O]\n")

        input("Başlamak İçin enter'a basın ")

        while (self.Oyun == self.Devam):  # Oyun devam ettiği sürece döngümüz devam edecek.

            self.tahtayı_çiz()  # Her turda tahtayı yeniden çizeceğiz.

            if (self.oyuncu % 2 != 0):  # Eğer sıra oyuncu-1 de ise işaret değeri 'X' olacak.
                print(f"Sıradaki oyuncu {oyuncu_1}")
                self.İşaret = 'X'

            else:  # Değilse 'O' olacak
                print(f"Sıradaki oyuncu {oyuncu_2}")
                self.İşaret = 'O'

            seçim = int(input("İşaretlemek için 1 ve 9 arasında bir sayı girin : "))

            if (self.boşluk_kontrol(seçim)):  # Eğer kullanıcını girdiği hücre boş değilse.

                self.tahta[seçim] = self.İşaret  # Seçilen hücreye kullanıcını işaretini koyduk.
                self.oyuncu += 1  # oyuncu değeri 1 arttı bu sayede ikiye bölümünden kalan değeri yani oyuncu  sırası değişti.
                self.durum_kontrol()  # Eğer devamdan farklı bir durum olursa Oyun değeri değişecek ve döngüye bir daha girilmeyecek.
                self.tahtayı_çiz()

                if (self.Oyun == self.Beraberlik):
                    print("* OYUN BERABERE *")

                elif (self.Oyun == self.Galibiyet):
                    self.oyuncu -= 1

                    if (self.oyuncu % 2 != 0):
                        print(f"* {oyuncu_1} KAZANDI *")

                    else:
                        print(f"* {oyuncu_2} KAZANDI *")

                        # Döngüden çıkıldığında yani oyun bittiğinde sonucu ekrana yazdırdık.


XOX()






