#Uebung Listen

NestedList = [[2,3,4],[0,6,1,4],[1,2]]
liste2 = NestedList[::-1]
print(liste2)
umkehr1= NestedList[0][::-1]
umkehr2= NestedList[1][::-1]
umkehr3= NestedList[2][::-1]


liste3 = umkehr1 + umkehr2 + umkehr3

print(liste3)
# for i in range(len(NestedList)): 
#     print(i)
#     print(NestedList[-2[-2]])



 