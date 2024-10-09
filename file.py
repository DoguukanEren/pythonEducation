# -*- coding: utf-8 -*-

# f = open("musteriler.txt")  #r durumu sadece okumak için , w durumu oluşturumak için,  a durumu ise dosyayı oku ve içine yeni birşeyler eklemek için , x durumu için de böyle bir dosya varsa kızar yoksa oluşuturur.

# # print(f.read())
# print("--------------------") # Eğer başta read aıp sonra okumaya çalışırsak tüm dosyayı okuduğu için devamını boş olarakj görür ReadLine Çalışmaz!
# print(f.readline()) #1.satır
# print(f.readline()) #2.satir
# print(f.readline()) #3.satir
# print(f.readline()) #4.satir

# for l in f :
#     print(f.readline())

# f.close()


# fileToAppend = open("ogrenciler2.txt","w") #w de dosyanın üzerine yazar önceki dosyanın içerğini kaybeder ekleneni ekler sadece

# fileToAppend.write("\n")
# fileToAppend.write("Salih")

# fileToAppend.close()


import os

os.remove("ogrenciler.txt")

os.rmdir() # Komutu ise klasörü silmek için kullanılmaktadır


