i=0
while i < 2:
  print(i)
  i=i+1
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
  
for x in range(2,6): # 2 6 arası yazdır
  print(x)

for x in range(2, 10, 3): # 2 den 30 a kadar 3 arttırarak yazdıor
  print(x)
  


for x in range(6):
  if x == 3: 
    break
  print(x)
else:
  print("Finally finished!")


ilk_metin = "asdasfddgdhfjfdgdşhjkjhkhjjh"
ikinci_metin = "sdfsuıdoryeuıfsjkdfhdjklghjdfklruseldhfjlkdshfljskeeuf"

for s in ikinci_metin: #ikinci_metin'deki, 's' adını verdiğimiz bütün öğeler için
    if not s in ilk_metin: #eğer 's' adlı bu öğe ilk_metin'de yoksa
        print(s) #'s' adlı öğeyi ekrana bas
