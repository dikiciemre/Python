


class araba():

    def __init__(self,marka,model,yil,renk):
        self.gelenmarka = marka
        self.gelenmodel = model
        self.gelenyil = yil
        self.gelenrenk = renk

    def bilgileriyazdir(self):
        print("marka: {}" .format(self.gelenmarka))
        print("model: {} ".format(self.gelenmodel))
        print("yil: {} " .format(self.gelenyil))
        print("renk: {} ".format(self.gelenrenk))
        print("---------------------------------------------------")

    def degistir(self, yil,renk):
        self.gelenyil = yil
        self.gelenrenk = renk


araba1 = araba("TOYOTA","COROLLA",2023,"gece yarısı")
araba2 = araba("Mercedes Benz","G63",2022,"inci beyazı")

araba1.bilgileriyazdir()
araba2.bilgileriyazdir()

araba2.degistir(2003,"turkuaz")
araba2.bilgileriyazdir()



