# -*- coding: utf-8 -*-
#UNİON BİRLŞEİM TEKRAR EDENLERİ ALMAZ

setA = {1,2,3,4,5}
setB = {3,4,5,6,7,8,9}

print(setA | setB)
print(setA.union(setB))
print(setB.union(setA))

#INTERSTECYION KESİŞİM OLANLARI ALIR

print(setA & setB)
print(setA.intersection(setB))
print(setB.intersection(setA))

#Diffrences A da olan b de olmayan 

print(setA - setB)
print(setA.difference(setB))
print(setB.difference(setA))

#symmetric_difference

print(setA ^ setB)
print(setA.symmetric_difference(setB))
print(setB.symmetric_difference(setA))