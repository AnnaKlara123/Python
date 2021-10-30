# Dreieck berrechnen

# moduls

import math

# Funktionen definieren

def length(dx, dy): # Funktion deniniert: sie erwartet 4 Argumente und inkludiert 3 Rechnungen 
    d = math.sqrt(dx**2 + dy**2)
    return d # d ist die Länge!

# Main --> Parameter definieren durch input 
dx = int(input("Geben  Sie die Erste Seitenlänge ein: "))
dy = int(input("Geben  Sie die zweite Seitenlänge ein: "))
iterat= int(input("Geben sie die Wiederholungen ein "))
weit = int(input("Schrittweite: "))

for i in range(0, iterat,1): # Schrittzahl eventuell später noch definieren
# Call function
    #schrittl = schrittl+liste[5]
    #var2 = dist(x1+schrittl,x2+schrittl, y1+i, y2+schrittl) # hier rechne ich immer PLUS die i-te Iteration 
    if i == 0:
        # dx = x2 - x1
        # dy = y2 -y1
        length1 = length(dx,dy)
        print(i)
        print("die Fläche beträgt: ", length1)
    else:
        dx = dx+weit 
        dy = dy+weit 
        length2 = length(dx,dy)
        print(i)
        print("die Fläche beträgt: ", length2)

# Main Inputs bekommen 
# liste = list(map(int, input("Gib 6 werte ein (x1, x2, y1, y2, der vorletzte Wert ist die Iterationslänge, der letzte Wert gibt die Schrittanzahl an: ").split())) # Eingabe als Liste einlesen 
# print(liste)
# #schrittl = 0 
# x1 = liste[0]
# x2 = liste[1]
# y1 = liste[2]
# y2 = liste[3]
# iterat = liste[4]

# for i in range(0, iterat,1): # Schrittzahl eventuell später noch definieren
# # Call function
#     #schrittl = schrittl+liste[5]
#     #var2 = dist(x1+schrittl,x2+schrittl, y1+i, y2+schrittl) # hier rechne ich immer PLUS die i-te Iteration 
#     var2 = dist(x1+i,x2+i, y1+i, y2+i) # hier rechne ich immer PLUS die i-te Iteration 
#     print(i)
#     print(var2)

#  # Direkte Berechnung mit vorgegebennen Zahlen 
#     # var1 = dist(1,2,3,4) # hier werden Argumente direkt der Funktion übergeben / Hier wird Funktuon aufgerufen
#     # print(var1)

