

class employeer():
    def __init__(self,name,surname,age,salary):
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = salary

    def getinfo(self):
        print("""
        KULLANICI BİLGİLERİ:
        {} {} çalışanının yaşı {} değerine sahiptir ve {} ₺ maaş almaktadır..
        """.format(self.name,self.surname,self.age,self.salary))

    def zamyap(self,salary): # maaşa %20 zam yapan fonksiyon
        self.salary = salary + (self.salary * 0.2)


class yonetici(employeer):#kaılıtım alınan yer
    pass


emre = employeer("Emre","Dikici",21,45_000)
emre.getinfo()

Buse = yonetici("Buse","Dikici",23,35_000)
Buse.getinfo()

emre.zamyap(45000) #mmaşına %20 zam yapılmış hali
emre.getinfo()







