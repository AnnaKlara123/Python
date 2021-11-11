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
i = 0 
def Dist(P1,P2,P3,P4):
    for i in ListeKoord:
        x1 = ListeKoord[i[0]]
        x2 = ListeKoord[i[1]]
        i+=1
        y1 = ListeKoord[i[0]]
        y2 = ListeKoord[i[1]]
        dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        return dist
def distanz(P1,P2,P3,P4):
    for i in len(ListeKoord):
        print(i)
        distance = math.sqrt( ((P1[0]-P2[0])**2)+((P1[1]-P2[1])**2) )

DistList = []

D12 = dist(P1, P2)
D13 = dist(P1, P3)
D14 = dist(P1, P4)
D23 = dist(P2, P3)
D24 = dist(P2, P4)
D34 = dist(P3, P4)
# print(dist(P1, P2))
# print(dist(P1, P3))

DistList.append(D12)
DistList.append(D13)
DistList.append(D14)
DistList.append(D23)
DistList.append(D24)
DistList.append(D34)

DistList.sort() # Sortiert die Liste
print(DistList)