# -*- coding: utf-8 -*-

#setler liste benzer daha hızlıdır sıralı değildir fakat unique yapılar içerir aynısından 2 tane kullanmazsın İndexi yok

studentSet = {"Doğukan","Hazal","İrey","Emre"}

print(studentSet)

for i in studentSet:
    print(i)
    

print("Hazal" in studentSet)


if "Hazal" in studentSet:
    print("Listede Var")
    
studentSet.add("Sait")
print(studentSet)

studentSet.update(["Merve","Selin"])
print(studentSet)

studentSet.remove("Selin")
print(studentSet)

studentSet.discard("Selin") # discard ise eğer sileceği nesneyi bulamazsa hata vermesin diye remove ile aynı olay
print(studentSet)

x = studentSet.pop() # Random bi eleman siler  #clear ile içini komple sileriz 
# del studentSet  # komple studentset i siler
print(studentSet) 