
"""
#büyük sayi
i=5
b=2
if i>b:
    print("i buyuk")
elif i==b:
    print("sayilar esit")
else: 
    ("b buyuk")
"""

"""
#liste içinde büyük sayi bulma 
sayilar=[1,2,3,4,5,6]
a=sayilar[0]
for x in sayilar:
    if a<x:
        a=x
else:
    print(a)
"""
"""
sayi=int(input("sayi giriniz "))
print(sayi)
"""



"""
def faktoriyel(sayi):
    snc=1
    while sayi>=1 :
        snc=sayi*snc
        sayi=sayi-1
    return snc


sayi2=int(input("sayi giriniz "))
print(faktoriyel(sayi2))
"""

"""
def faktoriyelfor(sayi):
    
    if sayi<0:
        print("negatif sayı hesplanamaz") 
        return 
    elif sayi==0 or sayi==1:
        return  1
    else:
        snc=1
        for i in range(1,sayi+1):
            snc=snc*i
    return snc
        

        
sayi=int(input("sayi giriniz : "))
print(faktoriyelfor(sayi))
"""

"""
sayilar=[1,2,3]
toplam=0
for i in range(0,len(sayilar)):
    toplam+=sayilar[i]
print(toplam)
"""

"""
sayilar=[1,2,3]
toplam=0
for i in range(len(sayilar)):
    toplam+=sayilar[i]
print(toplam)
"""


sayilar=[1,2,3,4,5]
sayilar2=[6,7,8,9,10]
toplam=[None] * len(sayilar)

for i in range(len(sayilar)):
    toplam[i]=sayilar[i]+sayilar2[i]
for i in range(len(toplam)):
    print(toplam[i])
