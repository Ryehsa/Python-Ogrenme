thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
"""""
print(thisdict) # bütün özellikleri yazdırma
print(thisdict["brand"]) # seçili özellik yazdırma
print(len(thisdict)) # kaç elemanlı olduğunu bulur
"""""
x = thisdict.keys() # başlıkları gösterir 
thisdict["year"] = 1990 # özellik değiştirme 
thisdict.update({"color": "red"}) # yeni özellik
print(x)
thisdict.popitem() # eklenen itemi kaldırma 
print(thisdict)