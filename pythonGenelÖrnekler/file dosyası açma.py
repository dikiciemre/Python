
#DOSYA OLUŞTURUP İÇİNE YAZI YAZDI

"""
dosya = open("EmreTextFile.txt","w")
print("Emre Dikici Python Öğreniyor",file=dosya )
"""



#hali hazırda olan dosyayı açar ve içine yazar YENİDEN DOSYA YARATMAZ !!!!
dosya = open("dosya.txt","a")
dosya.write("konya yolundayım\n")



#dosyanın içini gösterir
with open("dosya.txt") as dosya: # dosya varsayılan olarak r modunda açıldı
    for i in dosya:
        print(i)





