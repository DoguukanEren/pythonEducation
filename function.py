# -*- coding: utf-8 -*-
#%%
def selamVer(isim  = "Dostum"): #Buna bir şey kullanmazsa eğer default olarak Dostum yaz demek
    print("Merhaba" , isim)
    
def selamVer1(isim , soyisim = "Arkadaş"): #Zorunlu olmayan değeri bu şekilde sona vermeye dikkat et
    print("Merhaba",isim,soyisim)
    
selamVer("Salih")
selamVer1("Meryem")

#%%
def dikUcgenAlaniHesapla(a,b):
    return a*b/2

alan = dikUcgenAlaniHesapla(3,4)

print(alan)
#%% LAMBDA

dikUcgenAlaniHesapla2 = lambda a,b : a*b/2

print(dikUcgenAlaniHesapla2(3,4))

x = dikUcgenAlaniHesapla2 # Herhangi bir fonksiyonu bir değişkene eşitleyebiliriz

print(x(4,5))