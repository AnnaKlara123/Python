# Dreieck berrechnen

# moduls

# Funktionen
import math

def area(h, k): # Funktion deniniert: sie erwartet 2 Argumente und inkludiert 1 Rechnung
        O = (k/2)*h
        return O # ist die Fläche
     
# Main --> Parameter definieren durch input 
h = int(input("Geben  Sie die Höhe ein des Dreiecks:"))
k = int(input("Geben Sie Kantenlänge  der Grundseite ein:"))
iterat= int(input("Geben sie die Wiederholungen ein"))
weit = int(input("Schrittweite: "))

for i in range(0, iterat,1): # Schrittzahl eventuell später noch definieren
# Call function
    #schrittl = schrittl+liste[5]
    #var2 = dist(x1+schrittl,x2+schrittl, y1+i, y2+schrittl) # hier rechne ich immer PLUS die i-te Iteration 
    if i == 0:
        h = h+weit
        k = k
        area1 = area(h, k)
        print(i)
        print("die Fläche beträgt: ", area1)
    else:
        h = h+weit
        k = k+weit
        area2 = area(h, k)
        print(i)
        print("die Fläche beträgt: ", area2)