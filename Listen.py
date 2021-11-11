#Uebung Listen
print("Variante 1: Items aus Liste umgekehrt")
NestedList = [[2,3,4],[0,6,1,4],[1,2]]
print("Ursprüngliche Liste: ", NestedList)
outlist =[]  # Variante 1 # Leere Liste erstellen, die dann befüllt werden kann 
for i in NestedList:
    #print(i)
    outlist.insert(0,i) # gesammte Sequenz umkehren
print(outlist)

# Variante 2
print("Variante 2: Alles (Listen in Items) umgekehrt")

outlist1 =[]
outlist2 =[]

for i in NestedList:
    for j in i:
        outlist1.insert(0,j) # gesammte Sequenz plus einzelne Listen umkehren 
        # print(i,j, outlist1)
    outlist2.insert(0, outlist1) # kehrt auch die inneren Klammern um
    outlist1 = []  # Leert die outlist1 Liste wieder!
print(outlist2)

# Variante 3
print("Variante 3: Alles umgekehrt in einer Liste")

NestedList = [[2,3,4],[0,6,1,4],[1,2]]
liste2 = NestedList[::-1]
print(liste2)
umkehr1= NestedList[0][::-1]
umkehr2= NestedList[1][::-1]
umkehr3= NestedList[2][::-1]
liste3 = umkehr1 + umkehr2 + umkehr3

print(liste3)