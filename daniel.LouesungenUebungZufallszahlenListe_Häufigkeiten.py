#tuple

import random
import time

timebefore = time.time()

# Erstellt Liste von zufälligen Zahlen von 0 bis 1000. Schleife wird 1000 mal durchgeführt.
# Zufallzahl von 0 bis 1000 wird erstellt. An die Liste zufall wird die immer wieder neue variable a drangehängt
zufall = []
for i in range (1000):
    a = (int(random.random()*1000))
    zufall.append(a)

# print(zufall)

mylist = []

for i in zufall:
    # print("i =",i) # i sind jeweiligen Zahlen 
    # wenn es schon ein Tupel [i,zufall,count(i)] gibt, wird dieses zunächst gelöscht und anschließend ein neues Tupel hinzugefügt
    if (i,zufall.count(i)) in mylist: # ZUfallsliste nach Zahl i durchsuchen und alle i zählen 
        mylist.remove((i,zufall.count(i)))
        mylist.append((i,zufall.count(i)))
    else:
        mylist.append((i,zufall.count(i)))


mylist.sort()
print(mylist)

timeafter = time.time()
duration = timeafter - timebefore
print(duration)

print("done")
