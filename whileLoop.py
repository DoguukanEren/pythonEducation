
sehirler = ["Ankara","Sivas","Ereğli"]

#%% Break İntro
for i in sehirler:
    if i == "Sivas":
        break
    print( i , "için kod : " , i[0:3])
 #%% Continue İntro
 for i in sehirler:
     if i == "Sivas":
         continue
     print( i , "için kod : " , i[0:3])
#%% For Range
# for x in range(100):
#     print(x)
# for x in range(0,10):
#     print(x)   
for x in range(2,100,2):
     print(x)   