#Sequnzielle Datentypen - For-Schleifen
# for i in range(5):
#     print(i)

# for i in range(3,5,1):
#     print(i)

# print(range(1,10,2))

# Beispiel string (Zeichenketten)

satz = "Hallo Welt"
# for var in satz:
#     print(var)

# print("done.")
 # hier wird jeder Buchstabe einzeln iterriert und ausgegeben! 

anzahl = len(satz)
print(anzahl)
for i in range(anzahl):
    print(i)
    print(satz[i]) # jetzt wird jeder Buchstabe mit jew. anzahl-Zahl ausgegeben

print("done.")