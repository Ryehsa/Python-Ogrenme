a = "   Hello, World!"
b = "Hello, World!"
print(b[2:5]) # belirli aralıktaki karakterli alma
print(b[:5]) # baştan belirlenen yere kadar 
print(b[-5:-2])
print(b.upper()) # büyük harf
print(b.lower())# küçük harf
print(len(b)) # kelime boyutu
print(a.strip()) # baştaki boşluğu siler
print(a.replace("H", "J")) #bütün  H harflerni j ile değiştir

c="kemal"
d="kara"
e=c+" "+d
print(e)


quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

