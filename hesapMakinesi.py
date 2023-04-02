import hesapMakinesiModul as hesapla


print("İşlem Seçiniz: ")
print("1 : Topla ")
print("2 : Çıkarma ")
print("3 : Bölme ")
print("4 : Çarpma")

secenek = input("işlem seçiniz")

sayi1=int(input("Birinci Sayiyi Giriniz : "))
sayi2=int(input("İkinci Sayiyi Giriniz : "))


if secenek=="1":
    a=hesapla.topla(sayi1,sayi2)
    print(a)
elif secenek=='2':
    a=hesapla.cikar(sayi1,sayi2)
    print(a)
elif secenek=='3':
    a=hesapla.bol(sayi1,sayi2)
    print(a)
elif secenek=='4':
    a=hesapla.carp(sayi1,sayi2)
    print(a)
else:
    print("Hatalı Seçim")