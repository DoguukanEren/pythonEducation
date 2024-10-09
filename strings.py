# -*- coding: utf-8 -*-


#subString
print("****SubStrings****")
msg = "Merhaba Dünya"
print(msg[2:5])
newMsg = msg[:5]
print(newMsg)
print("-------------")
#----------------------#

#len(LENGTH)
print("****Length Fonksiyonu****")
print(len(msg))
newMsg1 = msg[len(msg)-1:len(msg)]
print(newMsg1)
#----------------------#

#Lower And Upper
print("****Lower And Upper****")
print(msg.upper())
print(msg.lower())
#----------------------#

#Replace
print("****Replace****")
print(msg.replace("ü", "u"))
print(msg.replace("a","e"))
#----------------------#

#Split
print("****Split****")
bilgi = "Doğukan Eren Özer 42 Konya"
print(bilgi.split())
print(bilgi.split("a")[1])
#----------------------#

#İnput
# print("****İnput****")
# ad = input("Adınız ?")
# sayi1 = input("Sayı1 =")
# sayi2 = input("Sayı2 =")

# print(int(sayi1)+int(sayi2))


