# -*- coding: utf-8 -*-
students = ["Doğukan", "Hazal" , "Kemal" , "Emre" , "Gökhan"]

students.append("Rana")
print(students)
print(students[2])
students.remove("Kemal")
print(students)

#list constructor

sehirler = list(("Ankara","Ereğli","Sivas"))
print(sehirler)
print(len(sehirler))

#Diğer Fonksiyonlar
# sehirler.clear()
print("Ankara Sayısı = " + str(sehirler.count("Ankara")))
print("Ankara'nın İndexi = " + str(sehirler.index("Ankara")))
sehirler.pop(1) # belirtilen indexi siler
print(sehirler)
sehirler.insert(1, "Ereğli")
print(sehirler)
sehirler.reverse()
print(sehirler)


sehirler2 = sehirler # Diziler Referans Tiptir Yani bu ikisi belleke aynı yeri işaret eder 
sehirler2[0] = "İzmir"
print(sehirler2)
print(sehirler)

sehirler3 = sehirler2.copy() # Bu kopyasını al demek eğer eşitlemek istiyorsan mutlaka kopyasını al 

sehirler.extend(students)
print(sehirler)

sehirler.sort()
print(sehirler)

sehirler.reverse()
print(sehirler)
