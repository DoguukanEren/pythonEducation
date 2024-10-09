# -*- coding: utf-8 -*-

ogrenciler = ["Doğukan","Eren","Özer","Hazal","Demir","Oğuzhan","İrey"]

fileToAppend = open("ogrenciler.txt","a")

for ogrenci in ogrenciler:
    fileToAppend.write(ogrenci)
    fileToAppend.write("\n")
    
fileToAppend.close()
    
    
