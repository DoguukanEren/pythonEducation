# -*- coding: utf-8 -*-

import sys

liste = [5,"Eren",0,12,"6"]

for sayi in liste:
    
    try:
        print("Sayı = " + str(sayi) )
        snc = 1/int(sayi)
        print("Sonuç = " + str(snc))
        
    except ZeroDivisionError:
        print(str(sayi) + "Böüm 0 olamaz.")
        
    # except ValueError:
    #     print(sayi , "Değeri bir sayı içermemektedir.")
        
    except:
        print(sayi,"Hesaplanamadı")
        print("Sistem Bir Hata Tespit Etti Lütfen Hata Kodu İle İlgili Birime Başvurunuz" , sys.exc_info()[0])
        
        
