# -*- coding: utf-8 -*-

#%% Azalan ve Çoğalan Üçgen
# num = int(input("Sayı Giriniz : "))
# star = "*"
# space = " "

# for i in range(1 , num):
    
#     space = space + star
    
#     print(space)
    
# for i in range(num):
    
#     spaceLength = len(space)
#     space = space[:-1]
#     print(space)
    
    
#%% Kelebek
num = int(input("Sayı Giriniz (2'nin katı olmalı): "))

if num % 2 != 0:
    print("Lütfen 2'nin katı bir sayı girin.")
else:
    # Üst yarı
    for i in range(num // 2):
        space = ' ' * ((num // 2 - i - 1))  # Boşluk hesaplama
        stars = '*' * (i * 2 + 1)            # Yıldız sayısı
        print(space + stars)

