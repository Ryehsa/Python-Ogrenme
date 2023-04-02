cars=["volvo","mereles","audi"] # dizi tanımlama


# diziye eleman ekleme
cars.append("tofaş") 
cars.insert(1,"totoş") # dizide belirli index e  eleman ekleme 
print(cars[1])
cars.pop(1) # diziden eleman silme
cars.remove("volvo")  # diziden eleman silme


for x in cars:   
    print(x)

