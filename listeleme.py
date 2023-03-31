thislist = ["apple", "banana", "cherry"] # liste tanımlama
print(thislist)

list1 = ["abc", 34, True, 40, "male"] # farklı değişken türünde değer atanabilir

thislist = ["apple", "banana", "cherry"]
print(len(thislist))   # listenin uzunluğun bulur

if "apple" in thislist:  # liste içi arama yapma
  print("Yes, 'apple' is in the fruits list")

mylist = thislist.copy() # liste kopyalama