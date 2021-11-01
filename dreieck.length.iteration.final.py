# Dreieck berrechnen

# moduls

import math

# Funktionen definieren

def length(dx, dy): # Funktion deniniert: sie erwartet 4 Argumente und inkludiert 3 Rechnungen 
    d = math.sqrt(dx**2 + dy**2)
    return d # d ist die Seitenlänge!

# Main --> Parameter definieren durch input 
dx = int(input("Geben  Sie die Erste Seitenlänge ein: "))
dy = int(input("Geben  Sie die zweite Seitenlänge ein: "))
iterat= int(input("Geben sie die Wiederholungen ein "))
weit = int(input("Schrittweite: "))

for i in range(0, iterat,1): # Schrittzahl eventuell später noch definieren
# Call function

    if i == 0:
        # dx = x2 - x1
        # dy = y2 -y1
        length1 = length(dx,dy)
        print(i)
        print("die Seitenlänge beträgt: ", length1)
    else:
        dx = dx+weit 
        dy = dy+weit 
        length2 = length(dx,dy)
        print(i)
        print("die Seitenlänge beträgt: ", length2)
