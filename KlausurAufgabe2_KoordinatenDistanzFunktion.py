# Geometrie: Längen der gegebenen 4 Punkte berechenen

from math import dist
from typing import List

# Punkte einlesen
P1 = [0, 3]
P2 = [5, 5]
P3 = [2, 4]
P4 = [2, 1]

ListeKoord = [P1]+[P2]+[P3]+[P4]

#print(ListeKoord)

# Funktion 
import math

# Länge der verbindenden strecken 
def Dist(P1,P2,P3,P4):
    for i in ListeKoord:
        print(i)
        x1 = ListeKoord[i[0]]
        x2 = ListeKoord[i[1]]
        i+=1
        y1 = ListeKoord[i[0]]
        y2 = ListeKoord[i[1]]
        dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        return dist
def distanz(ListKoord):
     distance1 = math.sqrt( ((P1[0]-P2[0])**2)+((P1[1]-P2[1])**2) )
     distance2 = math.sqrt( ((P1[0]-P3[0])**2)+((P1[1]-P3[1])**2) )
     distance3 = math.sqrt( ((P1[0]-P4[0])**2)+((P1[1]-P4[1])**2) )
     distance4 = math.sqrt( ((P2[0]-P3[0])**2)+((P2[1]-P3[1])**2) )
     distance5 = math.sqrt( ((P2[0]-P4[0])**2)+((P2[1]-P4[1])**2) )
     distance6 = math.sqrt( ((P3[0]-P4[0])**2)+((P3[1]-P4[1])**2) )
     # distanzList = [distance1,distance2, distance3, distance4, distance5, distance6]
     return distance1, distance2, distance3, distance4, distance5, distance6
Distanz1 = distanz(ListeKoord)
a, b, c, d, e, f = Distanz1 # tuple in Variablen speichern
DistanzListe = [a, b, c, d, e, f] # Variablen aus Tupel zur Liste machen

print(type(DistanzListe),"Liste")
DistanzListe.sort() # Liste nun sortierbar! 
print(DistanzListe)
print(type(Distanz1))
print(Distanz1)
#print(ListDistanz.sort())
