"""""
f=open("musteri.txt") # dosya açma
# 
# print(f.read())   # dosya okuma işlemi

#for l in f:
 #   print(l)

print (f.readline())   # satır okuma kodu
f.close() # dosya kapama işlemi

f=open("ogrenciler.txt","a") # a   append işlemi yani oluşturma 
f.write("Kemal") #  dosyaya yazla işlemi 
f.close()
"""""

"""""
# dsoya silme işlemi için

import os 
if os.path.exists("ogrenciler.txt"):
    os.remove("ogrenciler.txt")
else:
    print("dosya yok")
    
    """""

ogrenciler=["kemal","harun","kara"] 

f=open("ogrenciler.txt","a")     # dosyaya diziden veri ytazma 
for ogrenci in ogrenciler:
    f.write(ogrenci)
    f.write("\n") #alt satıra geçme

f.close()