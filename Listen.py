#Uebung Listen

NestedList = [[2,3,4],[0,6,1,4],[1,2]]
# meine Variante:  print(NestedList[::-1])
outlist =[]  # Prof Variante 1 # Leere Liste erstellen, die dann befüllt werden kann 
for i in NestedList:
    print(i)
    outlist.insert(0,i) # gesammte Sequenz umkehren

print(NestedList)
print(outlist)
print("done")

# Prof Variante 2

outlist1 =[]
outlist2 =[]

for i in NestedList:
    for j in i:
        outlist1.insert(0,j) # gesammte Sequenz plus einzelne Listen umkehren 
        print(i,j, outlist1)
    outlist2.insert(0, outlist1) # kehrt auch die inneren Klammern um
    outlist1 = []  # Leert die outlist1 Liste wieder!

print(NestedList)
print(outlist2)
print(outlist1)