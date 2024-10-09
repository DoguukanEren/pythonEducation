# -*- coding: utf-8 -*-
# tuple listeler ile aynı tiptedir fakat asıl olayı değiştirlemez liste tuttuğu için daha hızlı çalışmasını olanak sağlar

tupleListe = (2,4,6,(1,3,5),[])
liste = [2,4,6,"Ankara",[7,9,11],()]

liste[0] = "0"
# tupleListe[0] = "4" yapamazsın ReadOnly nesnedir

tupledeger = ("Engin",) # virgül olmadan string olarak algılar
print(type(tupledeger))


print(tupleListe[-2])
print(liste[-2])

print(tupleListe[1:2])
print(liste[1:2])

print(type(tupleListe))
print(type(liste))

print(tupleListe)
print(liste)






