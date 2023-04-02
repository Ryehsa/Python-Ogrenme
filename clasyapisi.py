"""""
class Mematik:
    def topla(self,sayi1,sayi2):
        return sayi1+sayi2
    
    def cikar(self,sayi1,sayi2):
        return sayi1-sayi2
    
    def carp(self,sayi1,sayi2):
        return sayi1*sayi2
    
    def bol(self,sayi1,sayi2):
        return sayi1/sayi2

islem=Mematik()
print(islem.carp(2,5))

"""

class Mematik:
    def __init__(self,sayi1,sayi2):
        
        self.sayi1=sayi1
        self.sayi2=sayi2

    def topla(self):
        return self.sayi1+self.sayi2
    
    def cikar(self):
        return self.sayi1+self.sayi2
    
    def carp(self):
        return self.sayi1+self.sayi2
    
    def bol(self):
        return self.sayi1+self.sayi2

islem=Mematik(2,5)
print(islem.carp())

#%% Property
