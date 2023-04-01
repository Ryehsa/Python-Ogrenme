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

