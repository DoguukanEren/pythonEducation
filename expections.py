# -*- coding: utf-8 -*-

try:
    num = int(input("Bir Sayı Giriniz"))
    
except ValueError: # (ValueError,ZeroDivisionError) şeklinde de belirtebiliriz beklentiyi
    print("Tip Uyuşmazlığı : Lütfen Bir Sayı Giriniz")
except ZeroDivisionError:
    print("Payda 0 Olamaz")
except:
    print("Bir Hata Oluştu")
    
print("Bitti")