

uyeler = { "uye" : ["Emre","Buse","Dikici"],
            "yaslar" : ["19","20","sonsuz"],}


print(uyeler["uye"])
print(uyeler["yaslar"])
print(uyeler)
print("------------------------------------------------------------------------------------------")

uyeler["superuye"] = ["Mustafa","Fatma"]
print(uyeler)
print("------------------------------------------------------------------------------------------")

uyeler["uye"] = ["Yeni","Uye"]
print(uyeler)
print("------------------------------------------------------------------------------------------")


print(uyeler.pop("yaslar"))#yas degerlerini bastırır
print("------------------------------------------------------------------------------------------")





"""
# dictionay yapısı örneği
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
print("------------------------------------------------------------------------------------------")

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




