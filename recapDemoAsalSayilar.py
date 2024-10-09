# -*- coding: utf-8 -*-

lastnum = int(input("Asal Olup Olmadığını öğrenmek istediğiniz sayı nedir ? "))
asalMi = True

for x in range(2,lastnum):
    
    if (lastnum % x == 0 ) :
        asalMi = False
        break
        
            
            
if asalMi:
    print("Asaldır")
    
else:
    print("Asal Değildir")