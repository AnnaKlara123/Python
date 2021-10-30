# Testen von seq.Datentypen 
werktage = ["Mo", "Di", "Mi","Do","Fr"]
#for Schleife
for tag in range(len(werktage)): # auf diese Weise kann ich auf den Index der Tupel zugreifen 
    print(tag)
    print(werktage[tag])
    if werktage[tag] == werktage[4]:
        print("done1")

# while Schleife
    i = 0  # hier arbeite ich mit einem count! 
while i < len(werktage):
  print(werktage[i])
  i = i + 1
  if i == len(werktage):
      print("done")


# print ("Liste inklusive Samstag: ", werktage)
# werktage.append("So")
# print ("Liste inklusive Samstag und Sonntag: ", werktage)
# werktage.reverse()
# print ("Die Liste Rueckwaerts: ", werktage)
# #sortieren
# werktage.sort()
# print ("Die Liste sortiert: ", werktage)