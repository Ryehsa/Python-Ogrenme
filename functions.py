def my_function(x): #sayilarla çalışma
  return 5 * x
print(my_function(5))


def ad_soyad(fname, lname): # iki değişkenle çalışma
  print(fname + " " + lname)

ad_soyad("mahmut","beyaz")


def my_functionfruit(food): # liste ile çalışma
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]
my_functionfruit(fruits)




def bilinmeyen_degisken_sayisi(*kids): 
  # birden fazla değer gönderirken fonksiyonda tanımlanan
  #  değişkenin başına * koyulur
  print("The youngest child is " + kids[2])

bilinmeyen_degisken_sayisi("Emil", "Tobias", "Linus")


def deger_atama_islemi(child3, child2, child1):
  
  print("The youngest child is " + child3)
#fonksiyona manuel değer atama işlemi
deger_atama_islemi(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


