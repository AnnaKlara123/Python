# uebung Tupel
import random


zufallsliste = [] # leere Liste erstellen, die später gefüllt werden kann
anzahl = {} # leeres Dictonary für die Häufigkeit des Auftretens 
for i in range (1000):
    a = int(random.random()*1000) # a ist eine Zahl aus der Random Liste bis 100 
    zufallsliste.append(a) # a wird der zufallsliste hinzugefügt 
#print(zufallsliste)
# print("break")
x = (0,1001) # zahl zwischen 0-1000 werden gecheckt
# iterating üner die Zufallsliste
for a in zufallsliste:
   #print(a)
   # checkt, ob die Zahl x(zwischen 0 -100) in der Zufallsliste vorkommt
   if x in zufallsliste: # Wenn die Zahl vorkommt dann:
      # Häufigkeit der Zahl bestimmen 
      anzahl = (anzahl[a]+ 1)
      a1= a
      print(a1)
   else:
      # wenn zahl nur 1x vorkommt 
      anzahl[a] = 1
# printing the frequency
print("Das Zufallsprogramm hat folgedes Dictionary erstelle::", anzahl)
# print("done")
# print(anzahl.keys()) Keys anzeigen lassen
print("Das Dictionary hat", len(anzahl), "Werte")
print("Das Dictionary hat", len(anzahl.keys()), "keys")

if len(anzahl) == len(anzahl.keys()):
   print("Kein Wert kommt doppelt vor")
else:
   print("Der Wert", a1, "kommt mehrmals vor")

