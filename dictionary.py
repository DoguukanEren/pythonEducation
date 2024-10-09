# -*- coding: utf-8 -*-

sozluk = {
           
            "book"  : "kitap",
            "table" : "masa"
    
         }

sozluk2 = dict(kitap = "book" , masa = "table")


sozluk["book"] = "yenikitap"
sozluk["pencik"] = "kalem"
print(sozluk["book"])
del(sozluk["book"])
print(sozluk)