# -*- coding: utf-8 -*-

from functools import reduce

sayilar = [1,2,3,4,5]
 
sayilarKareli = list(map(lambda sayi : sayi*sayi,sayilar))
sayilarFiltreli = list(filter(lambda sayi : sayi > 2 ,sayilar))
sayilarFaktoriyel = reduce(lambda x,y:x*y , sayilar)


# for sayi in sayilar:
#     sayilarKareli.append(sayi*sayi)
    
    
print(sayilarKareli)
print(sayilarFiltreli)
print(sayilarFaktoriyel)